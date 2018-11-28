#!/usr/bin/env python3
"""Google Code Jam Submission
Problem: 2011 Qualification Round C
Author: Matt Giuca
"""

import sys
import functools

def parse_input(infile):
    """Consume input for a single case from infile.
    Return list of ints.
    """
    n = int(infile.readline().strip())
    data = infile.readline().split()
    assert n == len(data)
    return list(map(int, data))

def psum(data):
    """Sum a sequence of integers, using Patricks' logic (XOR)."""
    return functools.reduce(lambda x,y: x^y, data)

def handle_case(data):
    """Given the data structure returned by parse_input, return 'NO' or the
    answer as an int.
    """
    # Trick question: Since Patrick's math is an XOR operation, moving candy
    # between the two piles applies the same operation to both. Therefore, for
    # any given input, Patrick will either be happy no matter what, or can
    # never be happy.
    # Thus, the algorithm is simple:
    # 1. Determine whether Patrick will be happy (if all numbers XOR to 0).
    # 2. Give him the smallest piece of candy.
    # 3. Sum all numbers and subtract the minimum value.
    if psum(data) != 0:
        # Patrick will never be happy.
        return 'NO'
    else:
        # Patrick will always be happy. Find the total value of the candy:
        total_candy = sum(data)
        # Give Patrick the smallest piece
        min_candy = min(data)
        return total_candy - min_candy

def main():
    numcases = int(sys.stdin.readline())
    for casenum in range(numcases):
        data = parse_input(sys.stdin)
        answer = handle_case(data)
        print("Case #{0}: {1}".format(casenum+1, answer))

if __name__ == "__main__":
    sys.exit(main())
