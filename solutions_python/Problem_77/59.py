#!/usr/bin/env python3
"""Google Code Jam Submission
Problem: 2011 Qualification Round D
Author: Matt Giuca
"""

import sys

def parse_input(infile):
    """Consume input for a single case from infile.
    Return list of ints.
    """
    n = int(infile.readline().strip())
    data = infile.readline().split()
    assert n == len(data)
    return list(map(int, data))

# The optimal strategy is to first compute the final sorted order in your
# head. Then, hold down all integers that are in the right place, and hit,
# to shuffle all others.
# Repeat until all sorted.
# For N integers out-of-place, the expected number of hits is N.

# Rationale:
# We abstract arrays as "N-out-of-place-arrays" (that is all that matters).
# An 5-array with 2 out of place is the same as a 2-array with 2 out of place,
# for example.
# For array N-out-of-place, we can work out the probabilities of obtaining
# each derived array in a single hit.
# For an array N, compute Pr(N to M) for all M <= N; these probabilities
# should sum to 1; note that Pr(N to 1) is always 0, since you cannot have a
# 1-out-of-place array.
# Compute the expected number of hits to sort the array E(N) from this:
# E(N) = 1 + Pr(N to 0)*E(0) + Pr(N to 2)*E(2) + ... + Pr(N to N-1)*E(N-1)
#        + Pr(N to N)*E(N)
# This is a recursive definition, but trivial rearrangement makes it
# computable:
# E(N) = (1 + Pr(N to 0)*E(0) + Pr(N to 2)*E(2) + ... + Pr(N to N-1)*E(N-1))
#        / (1 - Pr(N to N))

# Experimentation with N up to 4:
# For N = 0, trivially the expected number of hits = 0.
# N cannot be 1 (there cannot be a single element out of place).
# For N = 2, a single hit has the following probabilities:
#   Pr(2 to 0) = (1/2)
#   Pr(2 to 2) = (1/2)
# E(N) = (1 + (1/2)*0) / (1-(1/2)) = 2
# For N = 3, a single hit has the following probabilities:
#   Pr(3 to 0) = (1/6)
#   Pr(3 to 2) = (3/6)
#   Pr(3 to 3) = (2/6)
# E(N) = (1 + (1/6)*0 + (3/6)*2) / (1-(2/6)) = 3
# For N = 4, a single hit has the following probabilities:
#   Pr(4 to 0) = (1/24)
#   Pr(4 to 2) = (6/24)
#   Pr(4 to 3) = (8/24)
#   Pr(4 to 4) = (9/24)
# E(N) = (1 + (1/24)*0 + (6/24)*2 + (8/24)*3) / (1-(9/24)) = 4
# We can extrapolate that E(N) = N.

def handle_case(data):
    """Given a list of ints, return the expected number of hits to sort.
    """
    sortdata = sorted(data)
    # Return the number of elements that are not in the same place in the
    # sorted/unsorted versions.
    return len([i for i in range(len(data)) if data[i] != sortdata[i]])

def main():
    numcases = int(sys.stdin.readline())
    for casenum in range(numcases):
        data = parse_input(sys.stdin)
        answer = handle_case(data)
        print("Case #{0}: {1:.6f}".format(casenum+1, answer))

if __name__ == "__main__":
    sys.exit(main())
