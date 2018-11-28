#!/usr/bin/env python3
"""Google Code Jam Submission
Problem: 2011 Round 1C Problem A
Author: Matt Giuca
"""

import sys

### Input parsing ###

def parse_input(infile):
    """Consume input for a single case from infile.
    Input has the following format:
    Each test case begins with a line containing an integer N.
    The next N lines contain some test data.
    Return the N lines as a list of strings.
    """
    r, c = map(int, infile.readline().strip().split())
    lines = []
    for i in range(r):
        data = list(infile.readline().strip())
        assert len(data) == c
        # TODO: Add further processing for data here
        lines.append(data)
    return lines

### Algorithm ###

def handle_case(data):
    """Given the data structure returned by parse_input, return the answer as
    a string or stringable value.
    If parse_input is a generator, should manually call list() on data.
    Return data changed or None.
    """
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == '#':
                try:
                    if data[r][c+1] != '#':
                        return None # Impossible
                    if data[r+1][c] != '#':
                        return None # Impossible
                    if data[r+1][c+1] != '#':
                        return None # Impossible
                    data[r][c] = '/'
                    data[r][c+1] = '\\'
                    data[r+1][c] = '\\'
                    data[r+1][c+1] = '/'
                except IndexError:
                    return None     # Impossible
    return data

### Top-level ###

def format(data):
    return '\n'.join(''.join(r) for r in data)

def main():
    numcases = int(sys.stdin.readline())
    for casenum in range(numcases):
        data = parse_input(sys.stdin)
        answer = handle_case(data)
        print("Case #{0}:\n{1}".format(casenum+1,
            format(answer) if answer else "Impossible"))

if __name__ == "__main__":
    sys.exit(main())
