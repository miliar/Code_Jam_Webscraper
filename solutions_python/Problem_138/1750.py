#!/usr/bin/env python

import sys

def war(naomi, ken, naomi_strategy):
    assert len(naomi) == len(ken)

    i = 0
    total = len(naomi)
    score = 0

    while i < total:

        naomi_c, naomi_i = naomi_strategy(naomi, ken)
        naomi = naomi[:naomi_i] + naomi[naomi_i + 1:]

        ken_c, ken_i = ken_strategy(naomi_c, ken)
        ken = ken[:ken_i] + ken[ken_i + 1:]

        if naomi_c > ken_c: score += 1

        i += 1

    return score

def naomi_war(naomi, ken):
    return min(map(lambda x: (x[1], x[0]), enumerate(naomi)))

def naomi_deceitful(naomi, ken):
    # Try to force ken into using the max mass block.
    max_ken = max(ken)

    naomi_en = map(lambda x: (x[1], x[0]), enumerate(naomi))

    naomi_c, naomi_i = max(naomi_en)

    if naomi_c > max_ken:
        # Ken will choose the min if naomi's block is larger than all his blocks.
        min_ken = min(ken)

        naomi_diff = map(lambda x: (x[0] - min_ken, x[1]), naomi_en)
        options = filter(lambda x: x[0] > 0, naomi_diff)

        naomi_c, naomi_i = min(options)
        return max_ken + 0.00001, naomi_i
        

    # Find the minimum index in naomi's blocks
    #naomi_i = min(range(len(naomi)), key = lambda i: naomi[i])
    naomi_c, naomi_i = min(naomi_en)

    #if naomi_c > max_ken:
    #    return naomi_c, naomi_i

    return max_ken - 0.00001, naomi_i

def ken_strategy(naomi_chosen, ken):
    options = filter(lambda x: x[0] > 0, map(lambda y: (y[1] - naomi_chosen, y[0]), enumerate(ken)))

    if options:
        best = min(options)
        return best[0] + naomi_chosen, best[1]

    return min(map(lambda x: (x[1], x[0]), enumerate(ken)))
    # If we have at least one option, then choose the minimum; otherwise choose
    # the minimum out of the available blocks.
    #return min(options) + naomi_chosen if options else min(ken)

def main():
    T = int(sys.stdin.readline())

    for i in range(T):
        N = int(sys.stdin.readline())

        naomi = map(float, sys.stdin.readline().split())
        ken = map(float, sys.stdin.readline().split())

        s_deceitful = war(naomi, ken, naomi_deceitful)
        s_war = war(naomi, ken, naomi_war)

        print("Case #%d: %d %d" % (i + 1, s_deceitful, s_war))

main()
