#!/usr/bin/env python
infile = "A-large.in"
outfile = infile.split(".")[0] + ".out"

fsrc = open(infile, "r")
fres = open(outfile, "w")

T = int(fsrc.readline())

for t in range(T):
    N, K = [int(value) for value in fsrc.readline().split()]
    #print "===", N, K, "==="
    max = 2**N
    #print max
    K2 = K % max
    res = "Case #%s: " %(t+1, ) 
    
    if (K2 == 0) or (K2 != (max-1)): res += "OFF"
    else: res += "ON"
    
    res += '\n'
    #print res
    fres.write(res)

fsrc.close()
fres.close()