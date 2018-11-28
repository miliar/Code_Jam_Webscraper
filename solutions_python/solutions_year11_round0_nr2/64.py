#!/usr/bin/env python3
"""Google Code Jam Submission
Problem: 2011 Qualification Round B
Author: Matt Giuca
"""

import sys
import collections

def parse_input(infile):
    """Consume input for a single case from infile.
    Return (combiners, destructors, invocation), where:
        - combiners is a dict mapping two-element strings onto chars, in both
          directions. For example, 'QFT' creates two map entries
          'QF': 'T' and 'FQ': 'T'.
        - destructors is a multidict mapping chars to sets of chars, in both
          directions.
          For example, 'RF' creates two map entries 'R': 'F' and 'F': 'R'.
        - invocation is a string.
    """
    data = infile.readline().split()
    c = int(data[0])
    combiner_source = data[1:1+c]
    d = int(data[1+c])
    destructor_source = data[1+c+1:1+c+1+d]
    n = int(data[1+c+1+d])
    invocation = data[1+c+1+d+1]
    assert n == len(invocation)

    # Build the maps
    combiners = {}
    for c in combiner_source:
        src = c[0:2]
        dst = c[2]
        combiners[src] = dst
        combiners[src[::-1]] = dst
    destructors = collections.defaultdict(set)
    for d in destructor_source:
        destructors[d[0]].add(d[1])
        destructors[d[1]].add(d[0])
    return combiners, destructors, invocation

def handle_case(data):
    """Given the data structure returned by parse_input, return the answer as
    a string or stringable value.
    If parse_input is a generator, should manually call list() on data.
    """
    combiners, destructors, invocation = data
    stack = []

    for e in invocation:
        # Does this element combine with the one on top of the stack?
        if len(stack) > 0 and (stack[-1] + e in combiners):
            # Pop the stack and replace with the combined element
            stack[-1] = combiners[stack[-1] + e]
        # Does this element destroy any other in the stack?
        elif any(d in stack for d in destructors[e]):
            # Wipe the stack
            stack = []
        else:
            # Just push the element
            stack.append(e)

    # Print the final stack
    return '[{}]'.format(', '.join(stack))

def main():
    numcases = int(sys.stdin.readline())
    for casenum in range(numcases):
        data = parse_input(sys.stdin)
        answer = handle_case(data)
        print("Case #{0}: {1}".format(casenum+1, answer))

if __name__ == "__main__":
    sys.exit(main())
