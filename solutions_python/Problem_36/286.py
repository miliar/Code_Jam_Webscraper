#!/usr/bin/env python

welcome = "welcome to code jam"
#welcome = "jam"

N = int(raw_input())
#N = 1
for case in xrange(1, N+1):
    message = raw_input()
    #message = "jjamm"
    DP = [[0]*(len(welcome)+1) for i in xrange(len(message))]
    n = 0
    for i in xrange(len(message)-1, -1, -1):
        if message[i] == welcome[-1]:
            n+=1
        DP[i][1] = n

    for i in xrange(2, len(welcome)+1):
        n = 0
        for j in xrange(len(message)-2, -1, -1):
            if message[j] == welcome[-i]:
                n+=DP[j+1][i-1]
            DP[j][i] = n
    #print DP
    ans = DP[0][len(welcome)] % 1000
    ans = str(ans)
    while len(ans) < 4:
        ans = '0'+ans
    print "Case #" + str(case) + ": " + ans
