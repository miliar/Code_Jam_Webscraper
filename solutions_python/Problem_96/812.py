#!/usr/bin/env python

import collections
import itertools
import sys

def is_surprising(score):
    for pair in itertools.combinations(score, 2):
        if abs(pair[0] - pair[1]) > 1:
            return True
    return False

def number_of_surprising(scores):
    return sum(1 for score in scores if is_surprising(score))

PRECOMPUTED_SUMS = []

def precompute_sums():
    global PRECOMPUTED_SUMS

    for x in xrange(30 + 1):
        PRECOMPUTED_SUMS.append(set())

    for a in xrange(10 + 1):
        for b in xrange(10 + 1):
            for c in xrange(10 + 1):
                if a + b + c <= 30 and abs(a - b) <= 2 and abs(a - c) <= 2 and abs(b - c) <= 2:
                    PRECOMPUTED_SUMS[a + b + c].add(tuple(sorted((a, b, c))))

precompute_sums()

def possible_scores_for(score):
    return list(PRECOMPUTED_SUMS[score])

def solve(S, p, scores):
    googlers = []
    for _ in xrange(len(scores)):
        googlers.append([])

    for idx, score in enumerate(scores):
        googlers[idx].extend(list(possible_scores_for(score)))

    the_most = 0
    for possible_scores in itertools.product(*googlers):
        count = 0
        if number_of_surprising(possible_scores) != S:
            continue 
        
        for possible_score in possible_scores:
            if max(possible_score) >= p:
                count += 1

        the_most = max(the_most, count)

    return the_most
        

if __name__ == "__main__":
    infile = open(sys.argv[1])
    outfile = open('output.txt', 'w')

    no_cases = int(infile.readline())
    for idx, line in enumerate(infile):
        case = idx + 1
        params = [int(x) for x in line.split()]
        N, S, p = params[:3]
        scores = params[3:]

        count = solve(S, p, scores)

        output = "Case #%d: %d\n" % (case, count)
        outfile.write(output)
        print output

