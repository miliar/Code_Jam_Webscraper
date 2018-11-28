#! /usr/bin/env python

import os
import sys

#Start 
T = int(sys.stdin.readline().strip())
for t in range(T):
    L = sys.stdin.readline().strip().split()

    N = int(L[0])

    R = []
    P = []
    for i in range(N):
        R.append(L[2*i+1])
        P.append(int(L[2*i+2]))

    tO = 1
    tB = 1
    All = 0
    timeB = 0
    timeO = 0
    for i in range(N):
        #print "\n"
        #print "i: %s" % i
        if R[i] == 'O':
            tO = abs(P[i] - tO)
            if i > 0:
                if R[i-1] == 'B':
                    timeO = 0
            #print "tO:%s" % tO
            #print "timeO:%s" % timeO
            #print "i:%s" % i
            if i > 0:
                if R[i-1] == 'B':
                    #print "last"
                    if tO >= timeB:
                        #print "tO > timeB"
                        All += (tO - timeB + 1)
                        timeO += (tO - timeB + 1)
                    elif tO == 0:
                        #print "tO == 0"
                        All += 1
                        timeO += 1
                    else:
                        All += 1
                        timeO += 1
                else:
                    All += (tO + 1)
                    timeO += (tO + 1)
            else:
                All += (tO + 1)
                timeO += (tO + 1)
            #print "All:%s" % All
            tO = P[i]

        elif R[i] == 'B':
            #print "tB:%s" % tB
            #print "P[i]:%s" % P[i]
            tB = abs(P[i] - tB)
            #print "tB:%s" % tB
            if i > 0:
                if R[i-1] == 'O':
                    timeB = 0
            #print "P[i]:%s" % P[i]
            #print "tB:%s" % tB
            #print "timeB:%s" % timeB
            if i > 0:
                if R[i-1] == 'O':
                    if tB >= timeO:
                        All += (tB - timeO + 1)
                        timeB += (tB -timeO + 1)
                    elif tB == 0:
                        All += 1
                        timeB += 1
                    else:
                        All += 1
                        timeB += 1
                else:
                    All += (tB + 1)
                    timeB += (tB + 1)
            else:
                All += (tB + 1)
                timeB += (tB + 1)
            #print "All:%s" % All
            tB = P[i]
            
        #print "All:%s" % All

    print('Case #%d: %s' % (t+1, All))
