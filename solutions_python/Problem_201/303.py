from sys import stdin
import sys
if len(sys.argv) > 1:
    sys.stdout = open(sys.argv[1], 'w')

def each_case(N, K):
    a, na, na_1 = N, 1, 0  # na_1 = number of length (a-1)
    while K > (na + na_1):
        K -= (na + na_1)
        if a % 2:  #a odd, (a-1) even
            na = 2*na + na_1
        else:      #a even, (a-1) odd
            na_1 = na + 2*na_1
        a = int(a/2)

    if K > na:
        return int((a-1)/2), int((a-2)/2)
    else:
        return int(a/2), int((a-1)/2)

T = int(stdin.readline())
for t in xrange(1,T+1):
    N, K = map(int, stdin.readline().split())
    y, z = each_case(N, K)
    print 'Case #{}: {} {}'.format(t, y, z)
