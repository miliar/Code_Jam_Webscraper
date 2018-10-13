#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Problem

# You're watching a show where Googlers (employees of Google) dance, and then each dancer is given a triplet of scores by three judges. Each triplet of scores consists of three integer scores from 0 to 10 inclusive. The judges have very similar standards, so it's surprising if a triplet of scores contains two scores that are 2 apart. No triplet of scores contains scores that are more than 2 apart.

# For example: (8, 8, 8) and (7, 8, 7) are not surprising. (6, 7, 8) and (6, 8, 8) are surprising. (7, 6, 9) will never happen.

# The total points for a Googler is the sum of the three scores in that Googler's triplet of scores. The best result for a Googler is the maximum of the three scores in that Googler's triplet of scores. Given the total points for each Googler, as well as the number of surprising triplets of scores, what is the maximum number of Googlers that could have had a best result of at least p?

# For example, suppose there were 6 Googlers, and they had the following total points: 29, 20, 8, 18, 18, 21. You remember that there were 2 surprising triplets of scores, and you want to know how many Googlers could have gotten a best result of 8 or better.

# With those total points, and knowing that two of the triplets were surprising, the triplets of scores could have been:

# 10 9 10
# 6 6 8 (*)
# 2 3 3
# 6 6 6
# 6 6 6
# 6 7 8 (*)
# The cases marked with a (*) are the surprising cases. This gives us 3 Googlers who got at least one score of 8 or better. There's no series of triplets of scores that would give us a higher number than 3, so the answer is 3.
# Input

# The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line containing integers separated by single spaces. The first integer will be N, the number of Googlers, and the second integer will be S, the number of surprising triplets of scores. The third integer will be p, as described above. Next will be N integers ti: the total points of the Googlers.

# Output

# For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the maximum number of Googlers who could have had a best result of greater than or equal to p.

# Limits

# 1 ≤ T ≤ 100.
# 0 ≤ S ≤ N.
# 0 ≤ p ≤ 10.
# 0 ≤ ti ≤ 30.
# At least S of the ti values will be between 2 and 28, inclusive.
# Small dataset

# 1 ≤ N ≤ 3.
# Large dataset

# 1 ≤ N ≤ 100.
# Sample


# Input 
 	
# Output 
 
# 4
# 3 1 5 15 13 11
# 3 0 8 23 22 21
# 2 1 1 8 0
# 6 2 8 29 20 8 18 18 21

# Case #1: 3
# Case #2: 2
# Case #3: 1
# Case #4: 3


import sys


def best_ns(total):
    assert 0 <= total <= 30
    return (total+2) / 3

def best_s(total):
    if total > 28 or total < 2:
        return best_ns(total)
    # FIX: could simplify
    return (total+4) / 3


#for n in reversed(range(31)):
#    print n, best_ns(n), best_s(n)


count_skipped = False
for n, line in enumerate(sys.stdin):
    if not count_skipped:
        count_skipped = True
        continue

    vs = [ int(s) for s in line.split() ]
    N = vs[0]
    S = vs[1]
    p = vs[2]
    t = vs[3:]

    assert len(t) == N

    #print "S=%d  p=%d" % (S, p)
    ts = sorted(t, reverse=True)
    #print ts
    bns = [ best_ns(t) for t in ts ]
    #print bns
    # improvable = len(list(v for v in bns if v == p-1))
    improvable = sum(1 for t in ts if best_ns(t) == (p-1) and best_s(t) == (best_ns(t)+1))

    #print 'number of improvable triples', improvable

    a = sum(1 for v in bns if v >= p) + min(improvable, S)
    print 'Case #%d: %d' % (n, a)
