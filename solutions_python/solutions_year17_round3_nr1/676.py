from math import *

def ri():
    return int(raw_input().strip())

def ria(delim=" "):
    return [int(s) for s in raw_input().strip().split(delim)]

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

def main():
    t = ri()
    for c in xrange(t):
        n, k = ria()
        cakes = []
        for cake in xrange(n):
            r, h = ria()
            cakes.append((r, h))
        cakes.sort(key=lambda (r, h): r, reverse=True)

        gmax = 0
        for start in xrange(0, n - k + 1):
            clist     = [2 * cakes[i][0] * pi * cakes[i][1] for i in xrange(start, n)]
            rstart    = cakes[start][0]
            clist[0] += rstart ** 2 * pi
            wt        = [1] * len(clist)
            W         = k
            gmax      = max(gmax, knapSack(W, wt, clist, len(clist)))
        print "Case #{}: {}".format(c + 1, gmax)
    
main()

