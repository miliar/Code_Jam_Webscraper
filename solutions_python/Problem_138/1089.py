import random
from unittest import TestCase
from codejam2014.d_war import War
from codejam2014.functions import *

__author__ = 'tehsphinx'


class TestD(TestCase):
    file_prefix = 'd_'

    def setUp(self):
        pass

    def dis_test_stratey(self):
        numbers_naomi = '0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899'.split(' ')
        numbers_naomi = [float(x) for x in numbers_naomi]
        numbers_ken = '0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458'.split(' ')
        numbers_ken = [float(x) for x in numbers_ken]

        numbers_naomi.sort()
        numbers_ken.sort()
        dbg(n=numbers_naomi)
        dbg(k=numbers_ken)

        numbers = random.sample(range(10000), 2000)
        set1 = numbers[0::2]
        num_n = [x / 10000 for x in set1]
        num_k = [x / 10000 for x in list(set(numbers) - set(set1))]

        dbg(num_n)
        dbg(num_k)

    def dis_test_sample(self):
        file_suffix = '_sample'

        mt = War(self.file_prefix + 'input' + file_suffix, self.file_prefix + 'output' + file_suffix)
        result = mt.process()

        dbg(result)
        should_be = [
            'Case #1: 0 0',
            'Case #2: 1 0',
            'Case #3: 2 1',
            'Case #4: 8 4',
            'Case #5: 9 2',
            'Case #6: 2 1',
            'Case #7: 5 1',
            'Case #8: 9 1',
        ]

        self.assertListEqual(result, should_be)

    def dis_test_run_process(self):
        """
        rename to test_run_process to execute the real thing. input has to be in a_input.txt. output will be in a_output.txt
        """
        file_suffix = ''

        mt = War(self.file_prefix + 'input' + file_suffix, self.file_prefix + 'output' + file_suffix)
        mt.process()

    def test_run_process_large(self):
        """
        rename to test_run_process to execute the real thing. input has to be in a_input.txt. output will be in a_output.txt
        """
        file_suffix = '_large'

        mt = War(self.file_prefix + 'input' + file_suffix, self.file_prefix + 'output' + file_suffix)
        mt.process()

