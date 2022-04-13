import requests
from os import environ


class FastBillAPIController:
    def __init__(self, api_username, api_key, api_url='https://my.fastbill.com/api/1.0/api.php'):
        self.api_username = api_username
        self.api_key = api_key
        self.api_url = api_url

    @staticmethod
    def get_dates(start_month, end_month, year):
        return tuple(f'{year}-{month:02}-' for month in range(start_month, end_month + 1))

    def _post(self, payload, offset=0, results=None):
        all_results = results if results else []
        payload['OFFSET'] = offset
        payload['LIMIT'] = 100
        r = requests.post(url=self.api_url, auth=(self.api_username, self.api_key), json=payload)
        this_result = r.json()
        this_response = next(
            iter(this_result['RESPONSE'].values()))  # result has only one response in dict, get the first / only one
        all_results.extend(this_response)
        if len(this_response) >= payload['LIMIT']:
            self._post(payload, offset + payload['LIMIT'], results=all_results)
        return all_results

    def _get_service(self, service, year, month=None):
        payload = {'SERVICE': service,
                   'Filter': {}
                   }
        payload['Filter']['year'] = year
        if month:
            payload['Filter']['month'] = month
        return self._post(payload=payload)

    def get_expenses(self, year, month=None):
        return self._get_service(service='expense.get', year=year, month=month)

    def get_revenues(self, year, month=None):
        return self._get_service(service='revenue.get', year=year, month=month)

    def get_invoices(self, year, month=None):
        return self._get_service(service='invoice.get', year=year, month=month)


def main():
    from datetime import datetime
    now = datetime.now()
    fbc = FastBillAPIController(api_username=environ.get('API_USER'), api_key=environ.get('API_KEY'))

    revenues = []
    expenses = []
    invoices = []
    for year in (now.year, now.year - 1):
        revenues.extend(fbc.get_revenues(year=year))
        expenses.extend(fbc.get_expenses(year=year))
        invoices.extend(fbc.get_invoices(year=year))

    for year in (now.year, now.year - 1):
        for q, i in enumerate(range(0, 12, 3)):
            print(f'Einnahmen (Gutschriften) {year} Q{q + 1}: ', round(sum(item['SUB_TOTAL']
                                                                           for item in revenues
                                                                           if item['PAID_DATE'].startswith(
                fbc.get_dates(start_month=i + 1, end_month=i + 3, year=year)))))

            print(f'Einnahmen (Rechnungen) {year} Q{q + 1}: ', round(sum(item['SUB_TOTAL']
                                                                         for item in invoices
                                                                         if item['PAID_DATE'].startswith(
                fbc.get_dates(start_month=i + 1, end_month=i + 3, year=year)))))

            print(f'Vorsteuer {year} Q{q + 1}:', round(sum(item['VAT_TOTAL']
                                                           for item in expenses
                                                           if item['PAID_DATE'].startswith(
                fbc.get_dates(start_month=i + 1, end_month=i + 3, year=year))), 2))
            print('-' * 60)


if __name__ == '__main__':
    main()
