from config import *
import webscraper.orchestrator
import unittest
from unittest.mock import patch


class TestOrchestrator(unittest.TestCase):
    def test_make_problem_list(self):
        with patch('webscraper.orchestrator.simple_get') as mocked_get:
            mocked_get.side_effect = lambda url: "Some content" if url in VALID_URL else None

            problem_list = webscraper.orchestrator.make_problem_list()

            for valid_url in VALID_URL:
                mocked_get.assert_any_call(valid_url)
            self.assertEqual(problem_list, PROBLEM_LIST)
