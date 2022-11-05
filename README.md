# Companies House
A python wrapper around the [Companies House UK API](https://developer.companieshouse.gov.uk/api/docs/).

## Example usage

```python
from companieshouse import companieshouse

ch = companieshouse.init('YOUR_API_KEY')
ch.get_company_overview('COMPANY_NUMBER')

# returns a dict of company details as a requests.Response object
```

For further details, see the docs:

https://lewismunday.github.io/companieshouse/ - in progress

## Supported Endpoints
- [x] Company Overview
- [x] Company Filing History
- [x] Company Officers
- [x] Company Persons with Significant Control
- [x] Company Charges
## Installation

To install the companieshouseapi package, clone the repo by running:

```bash
git clone git://github.com/lewismunday/companieshouseapi.git
```

Then install the package by running:

```bash
python setup.py install
```


