#!/usr/bin/python

f = open('./A-large.in','r')

f.readline()
case = 0
for l in f:
    case += 1
    cnt, snaps = [int(n) for n in l.split()]

    needed = pow(2, cnt)-1
    happened = snaps & needed

    if happened == needed:
        print "Case #"+str(case)+": ON"
    else:
        print "Case #"+str(case)+": OFF"
