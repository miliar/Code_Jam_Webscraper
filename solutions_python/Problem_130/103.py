from math import log

def best_case(N, P):
    n = N
    r = 0
    while 2**n > P:
        r += 1
        n -= 1

    needed_below = 2**r -1
    return 2**N-needed_below-1

def worst_case(N,P):
    if P == 2**N:
        return 2**N -1
    
    x = 0.5
    r = 1
    while (2**N) * x < P:
        r += 1
        x += 1./2**r

    return 2**r -2
    
    
    

def solve(N, P):
    return worst_case(N,P), best_case(N,P)


if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1,T+1):
        N,P = map(int, raw_input().split())
        a,b = solve(N,P)
        print "Case #%d: %d %d" % (i, a,b)
