import math

def minkeys(p, k, l, probs):
    probs.sort()
    probs.reverse()
    if(k * p < l):
        return "Impossible"
    i = 0
    res = 0
    while i < l:
        res += (i/k+1) * probs[i]
        i += 1
    return res

ip = open("A-large.in", "r")
a = ip.readlines()
NoOfTestCases = int(a[0])
curline = 0
for i in range(NoOfTestCases):
    curline += 1
    curinp = a[curline]
    curinp = curinp.split()
    P = int(curinp[0])
    K = int(curinp[1])
    L = int(curinp[2])
    curline += 1
    curinp = a[curline]
    curinp = curinp.split()
    probs = []
    for j in curinp:
        probs += [int(j)]
    print "Case #%d:" % (i+1),
    print minkeys(P, K, L, probs)

    
