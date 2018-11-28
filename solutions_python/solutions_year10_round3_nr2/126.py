#!/usr/bin/env python

infile = "B-large.in"
#infile = "B-small-attempt1.in"
#infile = "B-sample.in"
outfile = infile.split(".")[0] + ".out"

f = open(infile, "r")
fres = open(outfile, "w")

T = int(f.readline())
#print T

for t in range(T):
    L, P, C = [int(value) for value in f.readline().strip().split()] 
    
    #print L, P
    arr = []
    val = L * C
    while val < P:
        arr.append(val)
        val *= C
    #print arr
    max = len(arr)
    count = 0
    #print 'Max:', max, 'C:', C
    if max != 0:
        while max > 1:
            max = max/2 
            count += 1
        count += 1
    res = "Case #%s: %s" %(t+1, count) 
    
    res += '\n'
    print res,
    fres.write(res)
    #raw_input()

f.close()
fres.close()
