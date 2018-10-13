#!/usr/bin/python
# -*-Python-*-
import sys
import string

def WriteAnswer(testNo, ans):
    print "Case #%d: %s" % (testNo, ans)

def TestCase(testNo):
    line =  sys.stdin.readline().split(" ")
    R = int(line[0])
    K = int(line[1])
    N = int(line[2])
    line =  sys.stdin.readline().split(" ")
    g = [int(i) for i in line]
    #print "R=", R, " K=", K, " N=", N, " g = ", g
    accum = 0
    car = []
    occup = 0
    l = list(g)
    rounds = 0
    for r in range(0, R):
        l = l + car
        car = []
        occup = 0
        first = l[0]
        while first != None:
            if (occup + first) > K:
                #print "car=", car, " first=", first, "l=", l
                #accum += occup
                #print "accum=", accum, " l=", l
                break
            else:
                #print "add ", first, " to ", car
                occup += first
                car += [first]
                l = l[1:]
                if not l: break
                first = l[0]
        #print "car=", car, " first=", first, "l=", l
        accum += occup
        #print "accum=", accum, " l=", l
    ans = accum
    WriteAnswer(testNo, ans)

# main
T = int(input())
for testNo in range(1, T+1):
   TestCase(testNo)
