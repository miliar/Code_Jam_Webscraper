'''
Created on 03/09/2009

@author: sebastian.serrano@gmail.com
'''
import re
import sys
import string
import numpy

f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()

out = open(sys.argv[1] + ".out", "w")

TOTAL = int(lines[0])

for case, line in enumerate(lines[1:]):
    N, K = map(int, line.split(" "))
    if numpy.all([(K/float(2**i) % 2) >=1 for i in xrange(N)]):
        out.write("Case #%d: ON\n" % (case+1))
    else:
        out.write("Case #%d: OFF\n" % (case+1))

out.close()





