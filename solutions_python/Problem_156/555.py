import math
import sys

T = input()
for case_num in range(1, T + 1):
    D = input()
    P = map(int, raw_input().split(" "))

    best = max(P)

    for max_stack_before_eat in xrange(1, max(P) + 1):
        num_specials_needed = 0

        for p in P:
            needed_for_p = math.ceil((1.0 * p) / max_stack_before_eat) - 1
            num_specials_needed += needed_for_p

        best = min(best, int(round(num_specials_needed + max_stack_before_eat)))

    print "Case #%d: %s" % (case_num, best)
