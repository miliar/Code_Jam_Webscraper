#!/usr/bin/python2

import collections

n = int(raw_input())
for i in range(1, n+1):
    line = raw_input()
    audience = line.split(" ")[1]
    # print(audience)
    val = [int(j) for j in str(audience)]
    standing = 0
    extra = 0
    for k in range(int(line.split(" ")[0])+1):
        if standing < k and val[k] > 0:
            # Fill what is required. 
            extra += (k - standing)
            standing += (k - standing)
            #print "in", extra
        standing += val[k]
        #print standing , "  " , extra
    print "Case #"+str(i)+ ":", extra
