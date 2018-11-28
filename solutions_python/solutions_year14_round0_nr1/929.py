#! /usr/bin/env python

from sys import stdin

ntest = input()

for test in xrange(ntest):
    cards = [0] * 16
    for i in xrange(2):
        row = input() - 1
        table = []
        for j in xrange(4):
            table.append([int(k) - 1 for k in stdin.readline().strip().split(' ')])
        for j in table[row]:
            cards[j] += 1
    guessed = [i+1 for i, j in enumerate(cards) if j == 2]
    if len(guessed) < 1:
        print "Case #{}: Volunteer cheated!".format(test+1)
    elif len(guessed) == 1:
        print "Case #{}: {}".format(test+1, guessed[0])
    else:
        print "Case #{}: Bad magician!".format(test+1)
