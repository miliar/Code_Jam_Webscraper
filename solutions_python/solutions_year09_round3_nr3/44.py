import sys
def permutations(L):
    if L == []:
        return [[]]
    else:
        return [[h]+t for i,h in enumerate(L)
                      for t   in permutations(L[:i]+L[i+1:])]

def simulate(release_order, P):
    occupied = [True for i in range(P)]
    c = 0
    for release in release_order:
        occupied[release-1]=False
        for i in range(release-2, -1, -1): #backword
            if occupied[i]:
                c+=1
            else:
                break

        for i in range(release, len(occupied)): #forward
            if occupied[i]:
                c+=1
            else:
                break
    return c
    
N = int(raw_input())
for X in range(1,N+1):
    P, Q = map(int, raw_input().split(' '))
    released = map(int, raw_input().split(' '))
    C = 0

    minC = sys.maxint
    for release_order_permutation in permutations(released):
        c = simulate(release_order_permutation, P)
        if c<minC:
            minC=c

    print 'Case #%d: %d' % (X, minC)
