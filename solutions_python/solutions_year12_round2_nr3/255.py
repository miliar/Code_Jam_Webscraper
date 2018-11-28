"""
Code jam round B question 3 
"""

import sys
import string

def load_tests(path):
    f = file(path)
    num_tests = int(f.readline())
    test_liness = f.readlines()
    assert num_tests == len(test_liness)
    tests = []
    for test_line in test_liness:
        numbers = [int(x) for x in test_line.split()]
        assert numbers[0] == len(numbers) - 1
        tests.append(numbers[1:])

    return tests

def find_sum(s, numbers):
    if s in numbers:
        return [s]
    
    for n in numbers:
        if s > n:
            subsum = find_sum(s - n, numbers - set((n,)))
            if subsum is not None:
                return [n] + subsum
            # not found reinstate n

def solve(numbers):
    numbers = sorted(numbers)
    numbers_set = set(numbers)
    result = None
    for i in xrange(1, 2**(len(numbers))):
        subset = set(numbers[j] for j in xrange(len(numbers)) if i & (1<<j))
        subset_sum = sum(subset)
        others = find_sum(subset_sum, numbers_set - subset)
        if others is not None:
            result = (subset, others)
            break
    
    if result is None:
        return 'impossible'
    else:
        return '\n' + ' '.join(str(i) for i in subset) + '\n' + ' '.join(str(i) for i in others)  
    
def main():
    tests = load_tests(sys.argv[1])
    
    test_num = 1
    for test in tests:
        print 'Case #%d:' % test_num, solve(test)
        test_num += 1
        
if '__main__' == __name__:
    main()