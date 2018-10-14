#!/opt/local/bin/python

import sys
from itertools import count
from fractions import Fraction

input_it = iter(sys.stdin.readlines())

T = int(input_it.next())

for case in range(T):
    N = int(input_it.next())
    results = []
    WPnumerators = []
    WPdenominators = []
    WPs = []
    for n in range(N):
        results_row = list(input_it.next())
        results.append(results_row) # as a string
        WPnumerator   = sum(1 for item in results_row if item == '1')
        WPdenominator = sum(1 for item in results_row if item in '01')
        WP = Fraction(WPnumerator, WPdenominator)
        WPnumerators.append(WPnumerator)
        WPdenominators.append(WPdenominator)
        WPs.append(WP)
    # print WPs

    OWPs = []
    for n in range(N):
        WPlist = [
            Fraction(WPnumerators[opp] - int(results[opp][n]), WPdenominators[opp] - 1)
            for opp in range(N) if results[n][opp] != '.'
        ]
        OWP = sum(WPlist) / len(WPlist)
        OWPs.append(OWP)
        # print '%s: %s' % (n, WPlist)
        # print '%s: %s' % (n, OWP)
    # print OWPs

    OOWPs = []
    for n in range(N):
        OWPlist = [OWPs[opp] for opp in range(N) if results[n][opp] != '.']
        OOWP = sum(OWPlist) / len(OWPlist)
        OOWPs.append(OOWP)
        # print '%s: %s' % (n, OOWP)
    # print OOWPs

    print 'Case #%s:' % (case + 1)
    for n in range(N):
        print '%1.10f' % float(WPs[n]/4 + OWPs[n]/2 + OOWPs[n]/4)

