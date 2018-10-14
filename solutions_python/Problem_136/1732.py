from decimal import *
import unittest
import cookie_clicker_alpha2 as cca

d = Decimal

class CookieClickerTest(unittest.TestCase):

    def setUp(self):
        cca.C = 500
        cca.F = 4
        cca.X = 2000

    def test_zero_farm_cost(self):
        self.assertEqual('%6f' % cca.farm_cost(0), '0.000000')

    def test_more_than_zero_farm_cost(self):
        self.assertEqual('%6f' % cca.farm_cost(1), '250.000000')
        self.assertEqual('%6f' % cca.farm_cost(2), '83.333333')

    def test_sum_farm_cost(self):
        self.assertEqual('%6f' % cca.sum_farm_cost(0), '0.000000')
        self.assertEqual('%6f' % cca.sum_farm_cost(1), '250.000000')
        self.assertEqual('%6f' % cca.sum_farm_cost(2), '333.333333')

    def test_win_cost(self):
        self.assertEqual('%6f' % cca.win_cost(0), '1000.000000')
        self.assertEqual('%6f' % cca.win_cost(1), '333.333333')
        self.assertEqual('%6f' % cca.win_cost(2), '200.000000')

    def test_sum_win_cost(self):
        self.assertEqual('%6f' % cca.sum_win_cost(3), '526.190476')

if __name__ == '__main__':
    unittest.main()
