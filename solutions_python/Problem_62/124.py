#!/usr/bin/env python

infile = "A-large.in"
#infile = "A-small-attempt1.in"
#infile = "A-sample.in"
outfile = infile.split(".")[0] + ".out"

fsrc = open(infile, "r")
fres = open(outfile, "w")

T = int(fsrc.readline())

for t in range(T):
    N = int(fsrc.readline())
    A = []
    B = []
    for i in range(N):
        a, b = [int(value) for value in fsrc.readline().split()]
        A.append(a)
        B.append(b)
    print A
    print B
    
    count = 0
    for i in range (N):
        for j in range(i+1, N):
            if (A[i] > A[j] and B[i] < B[j]) or (A[i] < A[j] and
                    B[i] > B[j]):
                count += 1

    res = "Case #%s: %s" %(t+1, count) 
    
    
    res += '\n'
    print res,
    fres.write(res)
    #raw_input('')

fsrc.close()
fres.close()
