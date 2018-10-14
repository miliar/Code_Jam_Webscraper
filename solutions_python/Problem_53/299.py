#! /usr/bin/env python

testfile = open("A-large.in").read().split('\n')
num_cases = int(testfile[0])

for case in xrange(num_cases):
    line = testfile[case+1].split()
    lights = int(line[0])
    snaps = int(line[1])
    if (snaps+1) % (2**lights) == 0:
        print "Case #%s: ON" %(case+1)
    else:
        print "Case #%s: OFF" %(case+1)
