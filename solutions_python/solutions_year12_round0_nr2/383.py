# -*- coding: utf-8 -*-
# 1. Есть 

# 1. Разбиваем на два множества: те, кто могли бы получить неожиданные оценки (score >= 2) и остальные
# 2. Среди тех, кто мог получить неожиданные оценки выбираем тех, кто мог преодолеть threshold без 
#

import sys


def maximalScore(scoreSum):
    return (scoreSum + 2) / 3

def maximalSurprizeScore(scoreSum):
    if scoreSum == 0:
        return 0
    return (scoreSum + 1) / 3 + 1

def solve(scoreSumSeq, surprizeCounter, threshold):
    result = 0
    for scoreSum in scoreSumSeq:
        if maximalScore(scoreSum) >= threshold:
            result += 1
        elif surprizeCounter > 0 and maximalSurprizeScore(scoreSum) >= threshold:
            surprizeCounter -= 1
            result += 1
    return result


numberOfCases = int(sys.stdin.readline())
for case in xrange(numberOfCases):
    tokenSeq = map(int, sys.stdin.readline().strip().split())
    N = tokenSeq[0]
    surprizeCounter = tokenSeq[1]
    threshold = tokenSeq[2]
    scoreSumSeq = tokenSeq[3:3+N]
    print "Case #%d: %d" % (case + 1, solve(scoreSumSeq, surprizeCounter, threshold))
