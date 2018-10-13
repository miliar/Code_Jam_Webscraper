from sys import stdin
import sys
if len(sys.argv) > 1:
    sys.stdout = open(sys.argv[1], 'w')

def each_case(N):
    last_tidy = ''
    nd = len(N)
    for d in xrange(nd):
        if int(N[d:]) < int(N[d] * (nd - d)):
            intN = int(N[d])
            assert intN > 0
            if intN > 1:
                last_tidy += str(intN-1)
            last_tidy += ('9'*(nd-d-1))
            break
        else:
            last_tidy += N[d]

    return last_tidy

T = int(stdin.readline())
for t in xrange(1,T+1):
    N = stdin.readline().strip()
    print 'Case #{}: {}'.format(t, each_case(N))
