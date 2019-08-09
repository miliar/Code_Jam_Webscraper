import unittest
from unittest.mock import patch
import pickle
import webscraper.scraper
from config import *


class TestScraper(unittest.TestCase):
    def setUp(self):
        with open("test/offline_test_page/test_main_page.p", "rb") as main, open("test/offline_test_page/test_sub_page.p", "rb") as sub:
            self.main_page = pickle.load(main)
            self.sub_page = pickle.load(sub)

    def test_get_all_downlad_links(self):
        def is_valid_url(url):
            if url == OFFLINE_MAIN_PAGE:
                return self.main_page
            elif url == OFFLINE_SUB_PAGE:
                return self.sub_page
            else:
                return None

        with patch('webscraper.scraper.simple_get') as mocked_get:
            mocked_get.side_effect = is_valid_url

            s = webscraper.scraper.Scraper('08', 0, 1, 'save_path_nr_1')
            download_links = s.get_all_download_links()
            sample_links = [download_links[n] for n in DOWNLOAD_LINKS_NR]

            self.assertEqual(sample_links, DOWNLOAD_LINKS)
