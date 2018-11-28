import pdb

T = int(raw_input())
for i in range(T):
    Smax, S = raw_input().split(' ')
    S = [int(x) for x in S]
    standing = S[0]
    needed = 0
    for j in range(1, int(Smax)+1):
        if S[j] > 0 and standing < j:
            needed += j-standing
            standing += needed
        standing += S[j]
    print "Case #"+str(i+1)+": "+str(needed)
