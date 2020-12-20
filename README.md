# fastbill-ustva

FastBill-UStVA is a Python script to get your preliminary tax report (Umsatzsteuervoranmeldung) done really quick using FastBill. 

It queries the FastBill API for revenues and expenses for the last and the current year and separates the output based on quarters by payment date.

Assumptions:

  - Based on payment date (Ist-Besteuerung)
  - Quarterly reports
  - Tax rate for outgoing invoices needs to be manually determined (usually 19%)


## Installation

Just clone the git folder and make sure that you set your FastBill API Credentials using Environment Variables:
 

```bash
export API_USER=your@email.com API_KEY=yourapikeynotyourpasswordcheckfastbillsettings
```

## Usage

```python
python3 main.py
```

```python
Einnahmen 2020 Q1:  1337
Vorsteuer 2020 Q1: 137.37
------------------------------------------------------------
Einnahmen 2020 Q2:  1337
Vorsteuer 2020 Q2: 137.37
------------------------------------------------------------
Einnahmen 2020 Q3:  1337
Vorsteuer 2020 Q3: 137.37
------------------------------------------------------------
Einnahmen 2020 Q4:  1337
Vorsteuer 2020 Q4: 137.37
------------------------------------------------------------
Einnahmen 2019 Q1:  1337
Vorsteuer 2019 Q1: 137.37
------------------------------------------------------------
Einnahmen 2019 Q2:  1337
Vorsteuer 2019 Q2: 137.37
------------------------------------------------------------
Einnahmen 2019 Q3:  1337
Vorsteuer 2019 Q3: 137.37
------------------------------------------------------------
Einnahmen 2019 Q4:  1337
Vorsteuer 2019 Q4: 137.37
------------------------------------------------------------
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)