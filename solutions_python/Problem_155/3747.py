import sys

T = int(sys.stdin.readline())
case = 1
for line in sys.stdin:
    (Smax, S) = line.split()
    Smax = int(Smax)
    S = [int(c) for c in S]
    standing = 0
    needed = 0
    for k in range(Smax+1):
        if standing < k and S[k] > 0:
            needed += k-standing
            standing += needed
        standing += S[k]
    print 'Case #{}: {}'.format(case, needed)
    case += 1
