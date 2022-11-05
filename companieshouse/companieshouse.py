import requests

API_URL = 'https://api.company-information.service.gov.uk'


class APIError(Exception):
    """Base class for exceptions in this module."""
    pass


class init:

    def __init__(self, api_key=None, company_number=None):
        self.API_KEY = api_key
        self.COMPANY_NUMBER = company_number

    def test_api(self):
        if self.API_KEY is None:
            try:
                raise APIError('API_KEY has not been set')
            except Exception as e:
                e.add_note('Please set API_KEY to your Companies House API key')
                raise

        response = requests.get(API_URL + '/company/04301762', auth=(self.API_KEY, ''))
        status_code = response.status_code
        description = response.reason
        error_description = None

        if status_code == 400:
            error_description = response.json()['error']

        print('{} - {}'.format(status_code, description if status_code != 400 else error_description))


    def get_company_overview(self, company_number=None):
        if company_number is None:
            company_number = self.COMPANY_NUMBER

        if company_number is None:
            try:
                raise APIError('COMPANY_NUMBER has not been set')
            except Exception as e:
                e.add_note('Please set COMPANY_NUMBER to your Companies House company number')
                raise
        response = requests.get(API_URL + '/company/' + company_number, auth=(self.API_KEY, ''))
        response = response.json()

        if 'errors' in response:
            error = response['errors'][0]['error']
            error = ' '.join(error.split('-')).title()  # Convert from "string-string" to "String String"
            raise APIError(error)

        return response

    def get_company_name(self, company_number=None):
        if company_number is None:
            return self.get_company_overview()['company_name']
        else:
            return self.get_company_overview(company_number)['company_name']

    def get_status(self, company_number=None):
        if company_number is None:
            company_number = self.COMPANY_NUMBER
            return self.get_company_overview()['company_status']
        else:
            return self.get_company_overview(company_number)['company_status']

    def is_active(self):
        return self.get_status() == 'active'

    def get_company_address(self, address_line_1=True, postal_code=True, locality=True, region=True):
        address = self.get_company_overview()['registered_office_address']

        if not address_line_1:
            address.pop('address_line_1')

        if not postal_code:
            address.pop('postal_code')

        if not locality:
            address.pop('locality')

        if not region:
            address.pop('region')

        return address

    def get_sic_codes(self):
        return self.get_company_overview()['sic_codes']

    def get_accounts(self):
        return self.get_company_overview()['accounts']

    def filing_history(self):
        link = self.get_company_overview()['links']['filing_history']
        response = requests.get(API_URL + link, auth=(self.API_KEY, ''))
        response = response.json()

        return response

    def get_officers(self):
        link = self.get_company_overview()['links']['officers']
        response = requests.get(API_URL + link, auth=(self.API_KEY, ''))
        response = response.json()

        return response['items']

    def get_charges(self):
        link = self.get_company_overview()['links']['charges']
        response = requests.get(API_URL + link, auth=(self.API_KEY, ''))
        response = response.json()

        return response

    def get_persons_with_significant_control(self):
        link = self.get_company_overview()['links']['persons_with_significant_control']
        response = requests.get(API_URL + link, auth=(self.API_KEY, ''))
        response = response.json()

        return response

    def get_exemptions(self, details=False):
        response = requests.get(API_URL + '/company/' + self.COMPANY_NUMBER + '/exemptions', auth=(self.API_KEY, ''))
        response = response.json()

        if response['errors'][0]['error'] == 'company-exemptions-not-found':
            if details:
                return 'No exemptions found'
            else:
                return False
        else:
            if details:
                return response['exemptions']
            else:
                return True

    def search(self, *query, items_per_page=10, start_index=0):
        response = requests.get(API_URL + '/search/companies?q=' + ' '.join(query) + '&items_per_page=' + str(items_per_page) + '&start_index=' + str(start_index), auth=(self.API_KEY, ''))
        response = response.json()

        return response


if __name__ == '__main__':
    ch = init()
