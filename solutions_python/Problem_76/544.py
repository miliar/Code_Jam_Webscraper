#!/usr/bin/env python

infile = "C-large.in"
#infile = "C-small-attempt0.in"
#infile = "C-sample.in"
outfile = infile.split(".")[0] + ".out"

fsrc = open(infile, "r")
fres = open(outfile, "w")

T = int(fsrc.readline())

for t in range(T):
    N = int(fsrc.readline())

    C = [int(value) for value in fsrc.readline().split()]

    ans = C[0]
    for c in C[1:]:
        ans ^= c

    if ans != 0:
        ans = 'NO'
    else:
        C.remove(min(C))
        ans = str(sum(C))

    res = "Case #%s: " %(t+1, ) 
    
    res += ans + '\n'
    print res,
    fres.write(res)

fsrc.close()
fres.close()
