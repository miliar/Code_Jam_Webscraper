#!/usr/bin/python

import string, sys

num_cases = int(sys.stdin.readline())

engines = []
queries = []

def init_from():
        return [0 for x in engines]

def transition_to (prev, query):
        prev_min = min(prev)
        next = [min(a, min(prev) + 1) for a in prev]
        next[engines.index(query)] = 9999; # fake +Inf
        # print "transition_to (" + str(prev) + ", " + str(query) + ") => " + str(next)
        return next

for case in range(num_cases):
        engines = []
        queries = []

        num_engines = int(sys.stdin.readline())
        for count in range(num_engines):
                engines.append(sys.stdin.readline().rstrip('\n'))
        # print "Got engines: " + str(engines)

        state = init_from()

        num_queries = int(sys.stdin.readline())
        for count in range(num_queries):
                query = sys.stdin.readline().rstrip('\n');
                state = transition_to(state, query)

        # print "End state: " + str(state)

        print "Case #" + str(int(case) + 1) + ": " + str(min(state))
