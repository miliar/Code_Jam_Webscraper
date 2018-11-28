#!/usr/bin/env python

import sys

def readline():
    return sys.stdin.readline().rstrip('\r\n')

def testcase():
    N = int(readline())
    outcome_map = {'1': 1., '0': 0., '.': None}
    outcome = []
    for team in range(N):
        outcome.append([outcome_map[c] for c in readline()])
    wins = [float(row.count(1.)) for row in outcome]
    games = [float(N-row.count(None)) for row in outcome]
    WP = [w/g for w,g in zip(wins, games)]
    OWP = []
    for team in range(N):
        other_WP = [
            (wins[other] - outcome[other][team]) / (games[other] - 1)
            for other in range(N)
            if outcome[team][other] is not None
            ]
        OWP.append(sum(other_WP) / len(other_WP))
    OOWP = []
    for team in range(N):
        other_OWP = [OWP[other] for other in range(N)
            if outcome[team][other] is not None]
        OOWP.append(sum(other_OWP) / len(other_OWP))
    return [0.25 * wp + 0.50 * owp  + 0.25 * oowp
        for wp, owp, oowp in zip(WP, OWP, OOWP)]

def main():
    n_cases = int(readline())
    for t_case in xrange(1, n_cases+1):
        print "Case #%d:" % t_case
        for value in testcase():
            print '%.12f' % value

if __name__ == '__main__':
    main()
