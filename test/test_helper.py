import webscraper.helper
import unittest
from unittest.mock import patch


class TestHelper(unittest.TestCase):

    def test_simple_get_good_response(self):
        with patch('webscraper.helper.get') as mocked_get:
            mocked_get.return_value.headers = {'Content-Type': 'html'}
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.content = 'Good Response'

            content = webscraper.helper.simple_get('Test-url')
            self.assertEqual(content, 'Good Response')

    def test_simple_get_bad_status_code(self):
        with patch('webscraper.helper.get') as mocked_get:
            mocked_get.return_value.headers = {'Content-Type': 'html'}
            mocked_get.return_value.status_code = 404

            content = webscraper.helper.simple_get('Test-url')
            self.assertEqual(content, None)

    def test_simple_get_bad_headers(self):
        with patch('webscraper.helper.get') as mocked_get:
            mocked_get.return_value.headers = {'Content-Type': 'zip'}
            mocked_get.return_value.status_code = 200

            content = webscraper.helper.simple_get('Test-url')
            self.assertEqual(content, None)
