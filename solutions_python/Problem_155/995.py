import sys
inp = sys.stdin.readline

def solve(S,A):
    tot = 0
    req = 0
    for i in xrange(S+1):
        if A[i] != 0:
            if tot >= i:
                tot += A[i]
            else:
                k = i - tot
                req += k                
                tot += A[i] + k
            # print req,tot
    return req

for i in xrange(1, int(inp().strip())+1):
    w = inp().strip().split()
    S = int(w[0])
    A = map(int, list(w[1]))
    print "Case #%d: %d" %(i,solve(S,A))