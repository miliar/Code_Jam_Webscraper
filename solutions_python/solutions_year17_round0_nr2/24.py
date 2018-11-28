import sys

def go(M):
    N = int(M)
    # Greedily add in up to 9 repunits
    # This is capable of producing all tidy numbers
    k = 9
    repunit = (10**20-1)/9
    x = 0
    while k>0 and repunit>0:
        x2 = x + repunit
        if x2 <= N:
            x = x2
            k -= 1
        else:
            repunit /= 10
    return x
    
#sys.stdin=open('datab.txt')

T=input()
for t in range(1,T+1):
    M=raw_input()
    print "Case #{}: {}".format(t,go(M))
