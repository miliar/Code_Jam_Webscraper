#!python
#-*- coding:utf-8 -*-

import sys

def solveA( a1, a2, N ):
    # decide win-able max index.
    wmis = []
    wmi = 0
    for a in a1:
        while wmi < N and a2[wmi] < a:
            wmi += 1
        wmis.append( wmi - 1 )
    
    used    = [ False for i in range(N) ]
    won_num = 0
    for i in range(N):
        # check win-able?
        for j in range( wmis[i] + 1 ):
            if not used[j]:
                # can win.
                used[j] = True
                won_num += 1
                break
        else:
            # cannot win. opponent will use highest value.
            for j in range( N - 1, -1, -1 ):
                if not used[j]:
                    used[j] = True
                    break
    return won_num

def solveB( a1, a2, N ):
    li = N - 1
    for i in range( N - 1, -1, -1 ):
        while li >= 0 and a1[li] > a2[i]:
            li -= 1
        if li < 0:
            return i + 1
        li -= 1
    return 0

T = int( sys.stdin.readline() )
for index in range(T):
    N = int( sys.stdin.readline() )
    a1 = [ float(x) for x in sys.stdin.readline().split() ]
    a2 = [ float(x) for x in sys.stdin.readline().split() ]
    a1.sort()
    a2.sort()
    print "Case #%d: %d %d" % ( index + 1, solveA( a1, a2, N ), solveB( a1, a2, N ) )
