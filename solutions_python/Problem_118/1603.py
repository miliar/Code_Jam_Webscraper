import fas
import unittest

class TestFairAndSquare(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, fas.fair_and_square_count(1, 4))

    def test_example2(self):
        self.assertEqual(0, fas.fair_and_square_count(10, 120))

    def test_example3(self):
        self.assertEqual(2, fas.fair_and_square_count(100, 1000))

    def test_big_numbers(self):
        self.assertEqual(26, fas.fair_and_square_count(1, 40000800004))

if __name__ == '__main__':
    unittest.main(exit=False)
