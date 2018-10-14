import sys
import math
import unittest

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def fair_and_square(A, B):
    a = int(math.ceil(math.sqrt(A)))
    b = int(math.floor(math.sqrt(B)))
    count = 0
    for n in xrange(a, b + 1):
        if is_palindrome(n) and is_palindrome(n**2):
            count += 1
    return count


class TestFairAndSquare(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(fair_and_square(1, 4), 2)

    def test_case_2(self):
        self.assertEqual(fair_and_square(10, 120), 0)

    def test_case_3(self):
        self.assertEqual(fair_and_square(100, 1000), 2)

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i, line in enumerate(sys.stdin, 1):
        A, B = map(int, line.split())
        result = fair_and_square(A, B)
        print "Case #%s: %s" % (i, result)
