from math import *

infile = open("B-large.in", "r")

T = int(infile.readline().strip())

for t in range(T):
    line = infile.readline()
    L = int(line.split(' ')[0])
    P = int(line.split(' ')[1])
    C = int(line.split(' ')[2])
    total = 0
    while (L * C < P):
        L *= C
        P = int(ceil(float(P) / float(C)))
        total += 2
        #print L, P
    if (L < P):
        total += 1
    #print total
    ans = int(ceil(log(total, 2)))
    print "Case #" + str(t+1) + ": " + str(ans);
