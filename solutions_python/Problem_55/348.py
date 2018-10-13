#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 et

import numpy
import sys

def read_numbers(input):
    return [ int(x) for x in input.readline().strip().split() ]

def main(input):
    testcases = int(input.readline().strip())
    for testcase in xrange(testcases):
        # R = rounds
        # k = how many people can it hold
        # N = groups
        R, k, N = read_numbers(input)
        g = numpy.array(read_numbers(input), dtype=numpy.int64)

        # pre-calculate the sums
        #print "Calculating s[][]..."
        s = numpy.empty((N,N), dtype=numpy.int64)

        for i in xrange(N):
            s[i][i] = 0

        for j in xrange(1,N+1):
            for i in xrange(N):
                s[i][(i+j) % N] = s[i][(i+j-1) % N] + g[(i+j-1) % N]

        # Now, s[i][j] contains the sum of elements from i until less than j
        # And s[i][i] contains the sum of all elements.

        # What to do when the queue starts at i?
        # next[i] -> the next start of the queue
        # income[i] -> the income of this round
        #print "Calculating next[] and income[]..."
        income = numpy.empty((N,), dtype=numpy.int64)
        next = [0] * N
        for i in xrange(N):
            for j in xrange(1,N+1):
                if s[i][(i+j) % N] > k:
                    break
                else:
                    income[i] = s[i][(i+j) % N]
                    next[i] = (i+j) % N

        # Cycle-detecting logic!
        # washere[i] -> the round when the queue started at this position
        # hadmoney[i] -> how much money we had at this point
        washere = [-1] * N
        hadmoney = [-1] * N

        #print "Start simulation..."
        total_income = 0
        current_round = 0
        queue = 0
        while current_round < R:
            if washere[queue] > -1:
                #print "Cycle detected on round %d (queue at %d)." % (current_round, queue)
                break
            else:
                #print "Round %d, queue from %d to %d, income = %d + %d." % (current_round, queue, next[queue], total_income, income[queue])
                washere[queue] = current_round
                hadmoney[queue] = total_income
                total_income += income[queue]
                queue = next[queue]
                current_round += 1

        if current_round < R:
            # Then a cycle was detected...
            cycle_length = current_round - washere[queue]
            cycle_income = total_income - hadmoney[queue]

            # Fast-forwarding through the cycle!
            remaining_rounds = R - current_round
            num_cycles = remaining_rounds // cycle_length
            total_income += num_cycles * cycle_income
            #print "Fast-forward through %d cycles for %d income." % (num_cycles, num_cycles*cycle_income)

            # Calculating the remaining rounds...
            current_round += num_cycles * cycle_length
            while current_round < R:
                total_income += income[queue]
                queue = next[queue]
                current_round += 1

        print "Case #%d: %d" % (testcase+1, total_income)

if __name__ == '__main__':
    main(sys.stdin)
