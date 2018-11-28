"""
Problem: Lawnmower


This script was written for Python 3.3.
It
 * reads from standard input
 * writes to standard output
 * logs to standard error

@author: Eric Dong
"""

# Python built-in libraries
import sys
import logging
import math
import numpy

# Log to standard error
logging.basicConfig(stream=sys.stderr, level=logging.INFO, \
                    format='%(asctime)s [%(levelname)-7s] %(message)s')

def main():
    
    mainmod = sys.modules['__main__']
    if mainmod and hasattr(mainmod, '__file__'):
        logging.info("Running {}".format(mainmod.__file__))

    cases = nextint()
    for case in range(1, cases+1):
        n, m = nextints()
        rows = []
        for r in range(n):
            rows.append(nextints())
            
        matrix = numpy.array(rows)
        logging.info("Case #%d: matrix: %s", case, matrix)
        result = solve(matrix, n, m)
        print("Case #{}: {}".format(case, result))
    sys.stdin.close()
        
def solve(matrix, n, m):
    """
    Solves for a single test case.
    """
    row_min = matrix.max(axis=1)
    col_min = matrix.max(axis=0)
    logging.info("Row mins: %s", row_min)
    logging.info("Col mins: %s", col_min)
    for (r, c), value in numpy.ndenumerate(matrix):
        if min(row_min[r], col_min[c]) != value:
                return "NO"
    
    return "YES"

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
       
if __name__ == '__main__':
    main()