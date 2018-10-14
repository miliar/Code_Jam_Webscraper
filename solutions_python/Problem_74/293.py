#!/usr/bin/env python

from sys import stdin

T = int(stdin.readline())

for CASO in xrange(1,T+1):
    l = stdin.readline().strip().split(" ")[1:]

    p = [1, 1]
    extra = [0, 0]
    total = 0

    for i in xrange(0, len(l), 2):
        if l[i] == 'O':
            bot = 0
        else:
            bot = 1

        pos = int(l[i+1])

        move = max(abs(pos-p[bot])-extra[bot]+1, 1)
        total += move
        p[bot] = pos

        extra[bot] = 0
        extra[abs(bot-1)] += move

    print "Case #%d: %d" % (CASO, total)
