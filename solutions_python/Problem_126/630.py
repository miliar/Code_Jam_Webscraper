"""
Problem: A


This script was written for Python 3.3.
It
 * reads from standard input
 * writes to standard output
 * logs to standard error

@author: edong
"""

# Python built-in libraries
import itertools
import logging
import math
import sys

# External libraries
# NumPY <http://www.numpy.org/>
#import numpy

# Log to standard error
level=logging.DEBUG
#level=logging.INFO
logging.basicConfig(stream=sys.stderr, level=level, \
                    format='%(asctime)s %(levelname)-7s %(message)s')

class TestCase(object):
    """
    Container for the inputs of a test case.
    """
    def __init__(self):
        pass
    
    def __str__(self):
        """
        Returns a representation.
        """
        return str(self.__dict__)
    
def parse_test_case():
    """
    Parses the inputs for a test case from standard input
    and returns the result.
    """
    case = TestCase()
    case.s, nstr = nextstr().split(' ')
    case.n = int(nstr)
    return case

def solve(case):
    """
    Solves a single test case, and returns the result.
    """
    s = case.s
    n = case.n
    length = len(s)
    
    was_vowel = False
    counts = []
    count = 0
    start = 0
    
    for i, c in enumerate(s):
        is_vowel = c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'
        if was_vowel != is_vowel:
            if count > 0:
                counts.append((count, was_vowel, start))
                
            count = 0
            was_vowel = is_vowel
            start = i
        
        count += 1
    counts.append((count, was_vowel, start))
    
    logging.info("Counts: %s", counts)
    
    total = 0
    
    for i in range(len(counts)):
        # Start from the left
        # Find first position where we find n consecutive
        first_match = None
        next_match = None
        for k in range(i, len(counts)):
            c = counts[k]
            if not c[1] and c[0] >= n:
                if first_match is None:
                    first_match = counts[k]
                    continue
                elif next_match is None:
                    next_match = counts[k]
                    break
        
        logging.debug("i=%d, first_match=%s, next_match=%s", i, first_match, next_match)
        
        if first_match is None:
            continue
        
        for start in range(counts[i][2], counts[i][2] + counts[i][0]):
            if first_match == counts[i]:
                if start <= counts[i][2] + counts[i][0] - n:
                    logging.debug("Special case: adding %d", length - (start + n - 1))
                    # Special case
                    total += length - (start + n - 1)            
                elif next_match is not None:
                    logging.debug("Special case: next adding %d", length - (next_match[2] + n - 1))
                    total += length - (next_match[2] + n - 1)
            else:
                logging.debug("Adding %d", length - (first_match[2] + n - 1))
                total += length - (first_match[2] + n - 1)
            
    return total
        

##############################################################
# Utility functions
        
def nextstr():
    """
    Returns the next line from standard input,
    without any trailing newlines.
    """
    l = sys.stdin.readline()
    if l[-1] == '\n':
        l = l[:-1]
    return l
    
def nextint():
    """
    Returns the next line from standard input as an integer.
    """
    return int(nextstr())

def nextints():
    """
    Returns the next line from standard input as a list of integers,
    where the input is split by ' '.
    """
    return [int(t) for t in nextstr().split(' ')]
    
def main():
    """
    Main function.
    """
    
    # Log module filename
    mainmod = sys.modules['__main__']
    if mainmod and hasattr(mainmod, '__file__'):
        logging.info("Running %s", mainmod.__file__)

    import time
    start_time = time.time()
    
    num_cases = nextint()

    for i in range(1, num_cases+1):
        test_case_start_time = time.time()
        case = parse_test_case()
        logging.info("Case #%d has inputs: %s", i, case)
        output = solve(case)
        print("Case #{}: {}".format(i, output))
        test_case_end_time = time.time()
        logging.info("Case #%d has output: %s", i, output)
        logging.debug("Case #%d running time: %0.1f s", \
                     i, test_case_end_time-test_case_start_time)
    sys.stdin.close()
    
    end_time = time.time()
    logging.info("Total running time: %0.1f s for %d test cases", \
                 end_time-start_time, num_cases)

if __name__ == '__main__':
    main()