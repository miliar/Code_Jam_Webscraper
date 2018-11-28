#!/usr/bin/python3

from common import *

def testcase(x):
    n, p = readintegers()
    players = 2 ** n

    if players == p:
        writeline("Case #%d: %d %d" % (x, players - 1, players - 1))
        return

    # The worst player that could win
    wins_needed = 0
    k = players
    while k > p:
        wins_needed += 1
        k = k // 2

    z = players - (2 ** wins_needed)

    # The best player that could lose
    losses_needed = 0
    k = players
    while k > (players - p):
        losses_needed += 1
        k = k // 2

    y = (2 ** losses_needed) - 1

    writeline("Case #%d: %d %d" % (x, y - 1, z))

run_tests(testcase)
