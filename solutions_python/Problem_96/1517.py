#!/usr/bin/python

import sys

def regular_lowest_total(m):
    """
    Given max score m, give lowest possible total possible for non-surprising triples
    """
    return max(3*m - 2, 0)

def surprising_lowest_total(m):
    """
    Given max score m, give lowest possible total possible for surprising triples
    """
    if m == 1:
        return 1
    else: 
        return max(3*m - 4, 0)

n = int(sys.stdin.readline().strip())
for i in range(1, n+1):
    tmp = map(int, sys.stdin.readline().strip().split())
    N, S, p = tmp[0], tmp[1], tmp[2]
    x = tmp[3:]
#    print 'N = %d, S = %d, p = %d, x = %s' % (N, S, p, x)
    x.sort()
#    print 'sorted x = %s' % (x)
    s_cutoff = surprising_lowest_total(p)


    x2 = filter(lambda z: z >= s_cutoff, x)

    answer1 = min(S, len(x2))
    
    x3 = x2[answer1:]
#    print "surprising cutoff = %d, selected %d, remaining: %s" % (s_cutoff, answer1, x3)

    r_cutoff = regular_lowest_total(p)

    x4 = filter(lambda z: z >= r_cutoff, x3)
    answer2 = len(x4)
#    print "regular cutoff = %d, selected %d (%s)" % (r_cutoff, answer2, x4)

    print "Case #%d: %d" % (i, answer1+answer2)
