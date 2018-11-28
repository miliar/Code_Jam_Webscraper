#!/usr/bin/env python

infile = "B-large.in"
#infile = "B-small-attempt1.in"
#infile = "B-sample.in"
outfile = infile.split(".")[0] + ".out"

fsrc = open(infile, "r")
fres = open(outfile, "w")

C = int(fsrc.readline())

for c in range(C):
    N, K, B, T = [int(value) for value in fsrc.readline().split()]
    x = [int(value) for value in fsrc.readline().split()]
    v = [int(value) for value in fsrc.readline().split()]
    print K, B 
    res = "Case #%s: " %(c+1, ) 
    
    if K == 0: res += str(0)
    else:
        #impossible check
        s1 = []
        for i in range(N):
            s1.append(v[i]*T + x[i])
        s = s1[:]
        s1.sort(reverse=True)
        print s

        if s1[K-1] < B: res += "IMPOSSIBLE"
        else:
            swaps = 0
            champs = 0
            for i in range(N):
                if s[N-i-1] < B: swaps += K-champs
                else: champs += 1
                if champs == K: break
            res += str(swaps)
        
    res += '\n'
    print res,
    fres.write(res)

fsrc.close()
fres.close()
