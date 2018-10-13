#!/usr/bin/python

import sys
import string

N = int(sys.stdin.readline())
for case in range(1,N+1):
    print "Case #%d:" % case,
    line = sys.stdin.readline()
    M = int(string.split(line)[0])
    shys = string.split(line)[1]
    up = 0
    needed = 0
#    print ""
    for i in range(0, M+1, 1):
        shyness = i
        num = int(shys[i])
 #       print "shyness:%d num:%d up:%d needed:%d " % (i, int(shys[i]), up, needed)
        if ( up < shyness and num > 0):
  #          print "%d < %d" % (up, shyness)
            needed += shyness - up
            up += shyness - up
        up += num
    print needed
