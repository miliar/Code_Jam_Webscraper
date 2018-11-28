#! /usr/bin/env python
import numpy

SENTENCE = 'welcome to code jam'
NUM_STATES = len(SENTENCE)

def analyze_sentence(s):
    slen = len(s)
    if slen < NUM_STATES: return 0
    sm = numpy.zeros((slen, NUM_STATES), dtype=numpy.int16) - 1
    for state in xrange(NUM_STATES):
        sm[slen - (NUM_STATES - state) + 1:, state] = 0
    def go(pos, state):
        if state == NUM_STATES: return 1
        if pos == slen: return 0
        if sm[pos, state] != -1:
            return sm[pos, state]
        count = go(pos + 1, state)
        if s[pos] == SENTENCE[state]:
            count += go(pos + 1, state + 1)
        count %= 10000
        sm[pos, state] = count
        return count
    #go(0,0)
    #print sm
    return go(0, 0)

if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(1, n + 1):
        line = raw_input()
        print 'Case #%d: %04d' % (i, analyze_sentence(line))
