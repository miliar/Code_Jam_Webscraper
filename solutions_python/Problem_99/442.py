# Google Code Jam 2012 round 1A
# typed 3 of 4
# p: 1 .9 .1
# enter first: 6 (1+4+1)
# keep typing: 2 7 (2+4+1)
# bs 1: 4 (1+2+1) 9 (4+4+1)
# bs 2: 6 (2+3+1) lose 11 (6+4+1)
# bs 3: 8 (3+4+1) lose
# Only need to evaluate keep typing and bs 1.
# keep typing: 2 * 1*.9*.1 + 7 * (1-1*.9*.1) = 2*.09 + 7*.91 = .18+6.37 = 6.55 lose
# bs 1: 4 * (1*.9) + 9 * 1-(1*.9) = 3.6 + .9 = 4.5 win
# Loop over number of bs, 0 to A.
# Divide psubn out of product of probs.
# expected = keysWin * prob + keyLose * (1-prob)
# save best expected, return after loop.

import sys
def mult(a,b): return a * b
def doCase(typed, total, probs):
    best = total + 2            # Enter right away
    prob = reduce(mult, probs)
    for numBS in range(typed):
        pWin = prob; pLose = 1-prob
        keysWin = numBS*2 + total - typed + 1
        keysLose = keysWin + total + 1
        expected = pWin * keysWin + pLose * keysLose
        best = min(best, expected)
        prob /= probs[-numBS-1]
    return best

def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        (typed,total) = map(int, file.readline().split())
        probs = map(float, file.readline().split())
        answer = doCase(typed, total, probs)
        print 'Case #{0}: {1}'.format(case, '%0.6f' % answer)
run()
