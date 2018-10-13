#!/usr/bin/env python

import collections
import sys

class Attempt(object):
    __slots__ = ['state', 'step']
    def __init__(self, state, step):
        self.state = state
        self.step = step
        
    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self, other):
        return hash(self.state)

def flipped(pancakes, size):
    for x in range(len(pancakes) - size + 1):
        yield pancakes[:x] + "".join('-' if x == '+' else '+' for x in pancakes[x:x + size]) + ''.join(pancakes[x + size:])

#for x in flipped('---', 1):
#    print x
#
#print '---'
#
#for x in flipped('---', 2):
#    print x

def solve(pancakes, size):
    if '-' not in pancakes:
        return 0

    step = 1
    mem = set([pancakes])
    attempts = [pancakes]
#    print pancakes
    while True:
        flips = set()
        for attempt in attempts:
            for f in flipped(attempt, int(size)):
                #print f
                if f in mem: continue
                if '-' not in f:
                    return step
                mem.add(f)
                flips.add(f)
        if not flips:
            return "IMPOSSIBLE"
        attempts = flips
        step += 1

input_lines = [l for l in open(sys.argv[1]).read().split('\n') if l]
input_lines = input_lines[1:]
for case, input_line in enumerate(input_lines):
    solution = solve(*input_line.split(' '))
    print "Case #{case}: {solution}".format(
        case=case + 1,
        solution=solution
    )
