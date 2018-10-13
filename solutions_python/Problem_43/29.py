'''
Created on Sep 13, 2009

@author: psyho
'''
import unittest

def minimum_base(str):
    min_base = len(set(str))
    return max(2, min_base)

def digits(base):
    result = range(base)
    result[0], result[1] = 1, 0
    return result

def to_int(digits, base):
    mult = 1
    sum = 0
    for digit in digits[::-1]:
        sum += (mult * digit)
        mult *= base
    return sum

def to_base(str):
    base = minimum_base(str)
    base_digits = digits(base)
    mapping = {}
    digit_idx = 0
    for c in str:
        if not(c in mapping):
            mapping[c] = base_digits[digit_idx]
            digit_idx += 1
    new_digits = [mapping[c] for c in str]
    return to_int(new_digits, base)

def main():
    T = int(raw_input())
    for i in xrange(T):
        str = raw_input().strip()
        print 'Case #%d: %d' % (i+1, to_base(str))

if __name__ == '__main__':
    main()
    
class ToBaseTest(unittest.TestCase):
    
    def testExampleA(self):
        self.assertEqual(201, to_base('11001001'))
    
    def testExampleB(self):
        self.assertEqual(75, to_base('cats'))
    
    def testExampleC(self):
        self.assertEqual(11, to_base('zig'))