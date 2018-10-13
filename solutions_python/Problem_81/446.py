#!/usr/bin/env python

from multiprocessing import Pool, cpu_count
from fractions import Fraction

def solve(params):

    WP = []
    for index, matches in enumerate(params):
        won = 0
        total = 0
        for match in matches:
            if match != '.':
                total += 1
            if match == '1':
                won += 1
        WP.append(Fraction(won, total))

    OWP = []
    for index, matches in enumerate(params):
        opponents = [i for i,v in enumerate(matches) if v != '.']
        OWP.append([])
        for o in opponents:
            won = 0
            total = 0
            for index2, match2 in enumerate(params[o]):
                if index2 == index:
                    continue
                if match2 != '.':
                    total += 1
                if match2 == '1':
                    won += 1
            OWP[index].append(Fraction(won, total))
        OWP[index] = sum(OWP[index])/Fraction(len(opponents), 1)


    OOWP = []
    for index, matches in enumerate(params):
        opponents = [i for i,v in enumerate(matches) if v != '.']
        OOWP.append([])
        for o in opponents:
            OOWP[index].append(OWP[o])
        OOWP[index] = sum(OOWP[index])/Fraction(len(opponents), 1)

    RPI = []
    for t in range(len(params)):
        RPI.append(Fraction(0, 1))
        RPI[t] += Fraction(1, 4)*WP[t]
        RPI[t] += Fraction(1, 2)*OWP[t]
        RPI[t] += Fraction(1, 4)*OOWP[t]

        #print RPI, RPI.numerator/float(RPI.denominator)

    return RPI

if __name__ == '__main__':
    T = int(raw_input())

    testcases = []
    for t in range(T):
        N = int(raw_input())
        table = []
        for n in range(N):
            line = raw_input().strip()
            line = list(line)
            table.append(line)
        testcases.append(table)

    pool = Pool(cpu_count())
    results = pool.map(solve, testcases)
    #results = [solve(t) for t in testcases]


    for t in range(T):
        print 'Case #{0}:'.format(t+1)
        for r in results[t]:
            print r.numerator/float(r.denominator)
