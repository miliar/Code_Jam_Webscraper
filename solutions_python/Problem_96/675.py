"""
Code jam qualification question 1 
"""

import sys
import string
from collections import defaultdict

def load_tests(path):
    f = file(path)
    num_tests = int(f.readline())
    lines = f.readlines()
    assert num_tests == len(lines)
    tests = []
    for test_line in lines:
        ints = [int(n) for n in test_line.split()]
        n = ints[0]
        s = ints[1]
        p = ints[2]
        
        totals = ints[3:]
        test = (n, s, p, totals)
        tests.append(test)
        
    return tests

def max_score(ts, is_surprise):
    remainder = ts % 3
    if remainder == 0:
        if is_surprise:
            if ts >= 3:
                return ts/3 + 1
            else:
                return # not possible
        else:
            return ts/3
    elif remainder == 1:
        if is_surprise:
            if ts >= 3:
                return ts/3 + 1
            else:
                return # not possible
        else:
            return ts/3 + 1
    else: #remainder == 2
        if is_surprise:
            return ts/3 + 2
        else:
            return ts/3 + 1
        

def solve(n, s, p, totals):
    count = 0

    for total in reversed(sorted(totals)):
        if max_score(total, False) >= p:
            count += 1
        else:
            if s == 0:
                # no more surprises
                return count
            else:
                max = max_score(total, True)
                if max is None:
                    continue
                
                if max >= p:
                    count += 1
                    s -= 1
    
    return count

def main():
    tests = load_tests(sys.argv[1])
    
    test_num = 1
    for test in tests:
        print 'Case #%d:' % test_num, solve(*test)
        test_num += 1
        
if '__main__' == __name__:
    main()