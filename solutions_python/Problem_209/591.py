#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
[Python 2.x]
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {} {}".format(i, n + m, n * m)
    # check out .format's specification for more formatting options

[Python 3.x]
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options
"""

def sort_by_value(d):
    return [ v for v in sorted(d.values())]



def surf_area(r, h):
    import math
    PI = math.pi
    return ((PI * (r ** 2)) + (2 * PI * r * h))

def surf_tuple(n, r, h):
    import math
    PI = math.pi
    return (n, r, h, (PI * (r ** 2)), (2 * PI * r * h), (PI * (r ** 2)) + (2 * PI * r * h))


def solve1(N, K, P):
    #print ("{DBG} N=%d, K=%d, P=%s" % (N, K, P))
    ST = {}
    n = 0
    for p in P:
        r, h = p
        ST[n] = surf_tuple(n, r, h)
        n += 1
    #print "{DBG}"
    #print ST
    #print "{DBG}---"
    sorted_ST = sorted(ST.iteritems(), key=lambda x: x[1][5], reverse=True)
    #print sorted_ST
    area = 0
    max_top = 0
    for p in sorted_ST[0:K]:
        area += p[1][4]
        if (p[1][3] > max_top):
            max_top = p[1][3]
    area += max_top
    return (area)



def surf_value_with_max_r(n, r, h, max_r):
    #print ("{DBG} n=%d, r=%d, h=%d, max_r=%d" % (n, r, h, max_r))
    import math
    PI = math.pi
    if (r > max_r):
        return (PI * (r ** 2)) - ((PI * (max_r ** 2))) + (2 * PI * r * h)
    else:
        return (2 * PI * r * h)


def solve(N, K, P):
    #print ("{DBG} N=%d, K=%d, P=%s" % (N, K, P))
    ST = {}
    n = 0
    best_n = None
    for p in P:
        r, h = p
        ST[n] = surf_tuple(n, r, h)
        if (best_n is None) or (ST[n][5] > ST[best_n][5]):
            best_n = n
        n += 1
    #print ("{DBG} best_n=%d" % (n))
    if (K == 1):
        return (ST[best_n][5])
    # find K-1 times the best choice
    area = ST[best_n][5]
    max_r = ST[best_n][1]
    ST.pop(best_n, None) # remove the best_n
    for k in xrange(K - 1):
        best_n = None
        best_s = 0
        for n in ST:
            r, h = ST[n][1], ST[n][2]
            s = surf_value_with_max_r(n, r, h, max_r)
            if (best_n is None) or (s > best_s):
                best_n = n
                best_s = s
        if (ST[best_n][1] > max_r):
            max_r = ST[best_n][1]
        #print ("{DBG} best_n=%d, best_s=%f" % (best_n, best_s))
        area += best_s
        ST.pop(best_n, None) # remove the best_n
    #sorted_ST = sorted(ST.iteritems(), key=lambda x: x[1][5], reverse=True)
    #print sorted_ST
    #area = 0
    #max_top = 0
    #for p in sorted_ST[0:K]:
    #    area += p[1][4]
    #    if (p[1][3] > max_top):
    #        max_top = p[1][3]
    #area += max_top
    return (area)





T = int(raw_input()) # read a line with a single integer

for t in xrange(1, T + 1):
    # each case `t`
    N, K = [int(s) for s in raw_input().split(" ")]  # read a list of integers
    P = []
    for n in xrange(N):
        (R, H) = [int(s) for s in raw_input().split(" ")]
        P.append((R, H))
    print "Case #{}: {:.9f}".format(t, solve(N, K, P))



