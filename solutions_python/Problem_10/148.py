from sys import *

def MinimumPresses(P, K, L, F):
    res = 0
    k = 1
    p = 0
    F.sort(reverse=True)
    for f in F:
        res += f * k
        p += 1
        if p % K == 0:
            k += 1
            p = 0
    return res

if __name__ == "__main__":
    N = int(stdin.readline().strip())
    for c in range(1, N + 1):
        P, K, L = map(int, stdin.readline().strip().split())
        F = map(int, stdin.readline().strip().split())
        print "Case #%d: %d" % (c, MinimumPresses(P, K, L, F))
    
    
    

    