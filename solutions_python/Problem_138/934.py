def successor(n, A):
    # A is sorted
    for a in A:
        if a > n:
            return a
    return A[0]

def normalWar(B, N, K):
    # if K has a block bigger than N, K plays the smallest block bigger than N
    # else, K plays the smallest block he has
    Kcopy = list(K)
    won = 0
    for n in N:
        k = successor(n, Kcopy)
        won += (n > k)
        Kcopy.remove(k)
    return won

def cheatWarImpl(B, N, K, Nstart, Nend, Kstart, Kend):
    # N is losing all the blocks that are smaller than K's smallest block
    # conversely, K is losing that number of his biggest blocks
    # if K has a bigger block than all of N, then N should say a weight just smaller than K and play her smallest
    # N can bait the smaller blocks by saying some arbitrarily large weight, and then play the smallest block that can beat it
    if B == 0:
        return 0
    smallestNIdx = 0
    while Nstart + smallestNIdx < Nend and N[Nstart + smallestNIdx] < K[Kstart]:
        smallestNIdx += 1
    eatIdx = 0
    while Nstart + smallestNIdx + eatIdx < Nend and N[Nstart + smallestNIdx + eatIdx] > K[Kstart + eatIdx]:
        eatIdx += 1
    return eatIdx + cheatWarImpl(
        B - smallestNIdx - eatIdx,
        N, K,
        Nstart + smallestNIdx + eatIdx,
        Nend,
        Kstart + eatIdx,
        Kend - smallestNIdx
    )
    
def cheatWar(B, N, K):
    return cheatWarImpl(B, N, K, 0, B, 0, B)


for _t in range(int(raw_input())):
    B = int(raw_input())
    N = sorted(map(float, raw_input().strip().split()))
    K = sorted(map(float, raw_input().strip().split()))
    
    print "Case #%d: %d %d" % (_t+1, cheatWar(B, N, K), normalWar(B, N, K))