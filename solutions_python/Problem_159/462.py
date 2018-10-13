import sys

T = input()

for t in xrange(T):
    input()
    M = raw_input().split()
    M = map(int, M)
    L = len(M)
    
    result1 = 0
    for i in xrange(L - 1):
        if M[i] > M[i + 1]:
            result1 += M[i] - M[i + 1]
    MAX = 0
    for i in xrange(L - 1):
        if MAX < M[i] - M[i + 1]:
            MAX = M[i] - M[i + 1]
    result2 = 0
    for i in xrange(L - 1):
        result2 += min(MAX, M[i])
    print 'CASE #{}: {} {}'.format(t + 1, result1, result2)
