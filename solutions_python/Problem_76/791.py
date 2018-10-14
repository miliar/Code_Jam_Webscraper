#!/usr/bin/python
import sys
argv = sys.argv
input = open(argv[1]).read().split("\n")
n = int(input.pop(0))
for i in xrange(n):
       num = int(input.pop(0))
       array = map(int,(input.pop(0).split(" ")))
       sumn = sum(array)
       minn = min(array)
       tmp = array[0]
       for j in xrange(1,num):
               tmp = tmp^array[j]
       if tmp != 0:
               print "Case #%s: NO" % (i+1)
       else:
               print "Case #%s: %s" % (i+1,sumn-minn)
