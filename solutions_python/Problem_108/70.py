#! /usr/bin/python -tt 

import sys
sys.path.append('/Users/hsiu/Documents/code/python')
import prime
import number_theory

T = input()
f = open("out", "w")
for Case in range(1, T+1):
    N = input()
    d = []
    l = []
    for i in range(N):
        aLine = raw_input()
        aLine = aLine.split()
        d.append(eval(aLine[0]))
        l.append(eval(aLine[1]))
    D = input()
    dp = [-1 for i in range(N)]
    dp[0] = 0
    print "Case:", Case
    for i in range(1, N):
        print "i = ", i
        for j in range(i):
            if 2*d[j] - dp[j] < d[i] or dp[j] == -1:
                continue
            sp = d[i] - min(d[i]-d[j], l[i])
            if sp < dp[i] or dp[i] == -1:
                dp[i] = sp
    #print dp
    reachable = False
    for i in range(N):
        if dp[i] == -1:
            continue
        if (2*d[i] - dp[i] >= D):
            reachable = True
            break
    if reachable:
        f.write("Case #%d: YES\n" % (Case))
    else:
        f.write("Case #%d: NO\n" % (Case))

