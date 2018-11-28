#!/usr/bin/env python
# Google Code Jam 2011
# Qualification Round
# Problem C - Candy Splitting
# May 7th 2011
# David Antliff <david.antliff@gmail.com>

import sys

def main():

    #input = sys.stdin
    input = open(sys.argv[1], 'r')

    test_cases = []

    # read input file
    T = int(input.readline())

    for i in range(T):
        N = int(input.readline())
        A = map(int, input.readline().split())
        test_cases.append(A)

    assert(len(test_cases) == T)

    # process test cases
    R = process_test_cases(test_cases)
    assert(len(R) == T)

    # print output file
    for i, r in enumerate(R):
        print("Case #%d: %s" % (i + 1, r))


def process_test_cases(test_cases):

    results = []
    num = len(test_cases)

    for i, case in enumerate(test_cases):
        sys.stderr.write("test case %d / %d\n" % (i + 1, num))
        r = split_candy(case)
        results.append(r)

    return results


import itertools

def split_candy(case):
    """
    Sean is very good at adding, and he wants to take as much value as
    he can without causing his little brother to cry. If it's
    possible, he will split the bag of candy into two non-empty piles
    such that Patrick thinks that both have the same value. Given the
    values of all pieces of candy in the bag, we would like to know if
    this is possible; and, if it's possible, determine the maximum
    possible value of Sean's pile.

    Additional info:
     - Sean can split the piles however he likes
     - Patrick 'adds' the piles in the original order

    Notes:
     - Patrick's adding mechanism is Exclusive OR
     - Exclusive OR is associative & commutative, so the order does not matter
     - values in test case are not always unique
    """

    s_best_sum = 0

#    print case
    if len(case) <= 1:
        return "NO"

    # annotate values to protect against duplicates
    annotated_case = [ (i, x) for i,x in enumerate(case) ]
#    print annotated_case

    for length in range(1, len(annotated_case)):
        for s_pile in itertools.combinations(annotated_case, length):
            p_pile = set(annotated_case).difference(s_pile)

            # unzip
            s_pile = zip(*s_pile)[1]
            p_pile = zip(*p_pile)[1]

#            print s_pile, p_pile

            s_sum = reduce(lambda x, y: x+y, s_pile)
            s_xor = reduce(lambda x, y: x^y, s_pile)
            p_xor = reduce(lambda x, y: x^y, p_pile)

#            print s_pile, s_sum, s_xor, p_pile, p_xor
            if s_xor == p_xor:
#                print "match"
                s_best_sum = max(s_sum, s_best_sum)

    return s_best_sum or "NO"


if __name__ == "__main__":
    main()
