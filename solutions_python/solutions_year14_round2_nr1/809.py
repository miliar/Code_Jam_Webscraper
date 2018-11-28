#! /usr/bin/python

import sys, itertools, re

def getline():
    return sys.stdin.readline().strip()

DEBUG = False
def out(s):
    if DEBUG:
        sys.stderr.write(str(s) + '\n')

class Case:
    pattern = re.compile(r'([a-z]{2,})')

    def __init__(self, casenum):
        self.casenum = casenum

    def done(self, answer):
        print 'Case #%d: %s' % (self.casenum, answer)

    def compress(self, word):
        last = None
        short = ''
        for letter in word:
            if letter != last:
                short += letter
            last = letter
        return short

    def calcVector(self, word):
        last = None
        vector = []
        for letter in word:
            if not last:
                count = 1
            elif last != letter:
                vector.append(count)
                count = 1
            else:
                count += 1
            last = letter
        vector.append(count)
        return vector

    def solve(self):
        n = int(getline())
        words = [getline() for x in xrange(n)]
        unique = set((self.compress(word) for word in words))

        if len(unique) > 1:
            self.done('Fegla Won')
            return

        vectors = [self.calcVector(word) for word in words]
        zipVectors = zip(*vectors)
        high = [max(v) for v in zipVectors]
        moves = 0
        for i in xrange(len(high)):
            mean = int(round(float(sum((min(j, high[i]) for j in zipVectors[i]))) / float(len(words))))
            for j in zipVectors[i]:
                moves += abs(j - mean)

        self.done(int(moves))

cases = int(getline())
for case in xrange(cases):
    Case(case + 1).solve()
