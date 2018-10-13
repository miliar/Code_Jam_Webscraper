#!/usr/bin/env python

import sys
import string
import operator

def possible_scores(total_score, max_deviation):
    """
        List all possible scores
    """
    def deviation(lst):
        l = sorted(lst)
        return l[-1] - l[0]

    low = total_score / 3
    base = [low, low, low]
    result = []
    maxdiv = max_deviation * 2 + 1
    for i in xrange(0, maxdiv**3):
        attempt = list(base)
        for j in xrange(0, 3):
            attempt[j] += i/maxdiv**j % maxdiv - max_deviation

        # No negative scores
        if len(filter(lambda n: n < 0, attempt)) == 0:
            # Total score adds up
            if total_score == reduce(lambda a, b: a + b, attempt):
                # Deviation rule
                if deviation(attempt) <= max_deviation:
                    result.append(attempt)
    return result
   
def num_winners(Surprises, p, total_scores):
    winners = 0
    surprisesleft = Surprises

    def p_in_list(p, lst):
        x = reduce(lambda a,b: a+b, lst)
        return len(filter(lambda a: a >= p, x)) > 0

    for total in total_scores:
        unsurprising = possible_scores(total, 1)
        surprising   = possible_scores(total, 2)

        if p_in_list(p, unsurprising):
            winners += 1
        elif p_in_list(p, surprising) and surprisesleft > 0:
            winners += 1
            surprisesleft -= 1
        else:
            # loser
            pass
    return winners

if __name__ == "__main__":
    # Read input
    numtests = int(sys.stdin.readline())
    for i in xrange(0, numtests):
        line = sys.stdin.readline().rstrip()
        # N    Number of googlers
        # S:   Number of surprising triplets
        # p:   Best result of at least ...
        # t:   Total points of the googlers
        N, S, p, t = line.split(" ",3)
        N, S, p = int(N), int(S), int(p)
        t = map(lambda n: int(n), t.split())
        result = num_winners(int(S), int(p), t)
        print "Case #%d: %d" % (i+1, result)

# vim:set expandtab tabstop=4 shiftwidth=4 softtabstop=4 nowrap:

