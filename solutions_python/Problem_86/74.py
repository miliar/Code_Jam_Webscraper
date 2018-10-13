#!/usr/bin/env python3
"""Google Code Jam Submission
Problem: 2011 Round 1C Problem C
Author: Matt Giuca
"""

import sys

### Input parsing ###

def parse_input(infile):
    """Consume input for a single case from infile.
    Input has the following format:
    Each test case is described in two lines. The first line contains a single
    integer N. The next line contains the N integers Ci separated by single
    spaces.
    Return the list of ints.
    """
    n, l, h = map(int, infile.readline().strip().split())
    data = infile.readline().split()
    assert n == len(data)
    return l, h, list(map(int, data))

### Algorithm ###

def trynote(note, others):
    for o in others:
        if note%o != 0 and o%note != 0:
            return False
    return True

def handle_case(data):
    """Given the data structure returned by parse_input, return the answer as
    a string or stringable value.
    If parse_input is a generator, should manually call list() on data.
    """
    l, h, others = data
    for note in range(l, h+1):
        if trynote(note, others):
            return note
    return None

### Top-level ###

def main():
    numcases = int(sys.stdin.readline())
    for casenum in range(numcases):
        data = parse_input(sys.stdin)
        answer = handle_case(data)
        print("Case #{0}: {1}".format(casenum+1, answer if answer is not None else "NO"))

if __name__ == "__main__":
    sys.exit(main())
