import sys
from collections import defaultdict
def ints():
    return [int(x) for x in raw_input().strip().split()]

#line = raw_input().strip()

T = input()
for t in range(T):
    N,P = ints()
    G = ints()
    #G = [g%P for g in G]
    M = [0]*P
    for g in G:
        M[g%P] += 1
    soln = M[0]
    if P == 2:
        soln += (M[1] + 1) / 2
    if P == 3:
        x = min(M[1], M[2])
        soln += x
        y = max(M[1], M[2]) - x
        soln += (y + 2) / 3
    if P == 4:
        soln += M[2] / 2
        x = min(M[1], M[3])
        soln += x
        y = max(M[1], M[3]) - x
        if M[2] % 2:
            y += 2
        soln += (y + 3) / 4
        #print "x",x,"y",y

    print "Case #%d: %d" % (t+1, soln)


    
    
