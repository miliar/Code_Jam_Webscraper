#!/usr/bin/env python3
"""Google Code Jam Submission
Problem: 2011 Round 1A Problem A
Author: Matt Giuca
"""

import sys

### Input parsing ###

def parse_input_list_ints(infile):
    """Consume input for a single case from infile.
    Input has the following format:
    Each test case is described in two lines. The first line contains a single
    integer N. The next line contains the N integers Ci separated by single
    spaces.
    Return the list of ints.
    """
    n = int(infile.readline().strip())
    data = infile.readline().split()
    assert n == len(data)
    return list(map(int, data))

def parse_input_list_lines(infile):
    """Consume input for a single case from infile.
    Input has the following format:
    Each test case begins with a line containing an integer N.
    The next N lines contain some test data.
    Return the N lines as a list of strings.
    """
    n = int(infile.readline().strip())
    lines = []
    for i in range(n):
        data = infile.readline().strip()
        # TODO: Add further processing for data here
        lines.append(data)
    return lines

def parse_input_custom(infile):
    """Consume input for a single case from infile.
    Return or yield a data structure describing the input.
    """
    data = infile.readline().split()
    assert 3 == len(data)
    return tuple(map(int, data))

# Set this to the appropriate input function above
parse_input = parse_input_custom

### Algorithm ###

def handle_case(data):
    """Given the data structure returned by parse_input, return the answer as
    a string or stringable value.
    If parse_input is a generator, should manually call list() on data.
    """
    n, pd, pg = data
    # Special cases:
    if pg == 0 and pd > 0:
        return False
    if pg == 100 and pd < 100:
        return False
    # Otherwise, ignore pg -- we can always make G large enough to make it
    # exact
    if n > 100:
        # Always possible, with D = 100, G = 10000, and the percentages exact
        #print("d = 100, won {0}, g = 10000, won {1}".format(pd, pg*100))
        return True
    else:
        # Brute force
        for d in range(1, n+1):
            if ((d * pd) % 100) == 0:
                # D = d, G = 100, and the percentages exact
                #wong = d * pg     # So > d and multiple of pg
                #g = int(wong * 100 / pg) if pg > 0 else 1
                #print("d = {0}, won {1}, g = {2}, won {3}".format(
                #    d, int(d * pd / 100), g, wong))
                return True

### Top-level ###

def main():
    numcases = int(sys.stdin.readline())
    for casenum in range(numcases):
        data = parse_input(sys.stdin)
        answer = handle_case(data)
        print("Case #{0}: {1}".format(casenum+1, "Possible" if answer else "Broken"))

if __name__ == "__main__":
    sys.exit(main())
