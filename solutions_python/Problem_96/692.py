#!/usr/bin/env python

from sys import stdin

for case in range (int(stdin.readline())):
    data = map(int, stdin.readline().split())
    numberOfGooglers = data[0]
    numberOfSurprises = data[1]
    p = data[2]
    totalScores = data[3:]
    answer = 0
    for score in totalScores:
        leftover = score - p
        avgRemainingScore = leftover / 2
        if avgRemainingScore < 0:
            continue
        if avgRemainingScore >= p:
            answer += 1
        elif p - avgRemainingScore == 1:
            answer += 1
        elif p - avgRemainingScore == 2:
            if numberOfSurprises > 0:
                answer += 1
                numberOfSurprises -= 1
    print "Case #%d: %s" % (case + 1, answer)
