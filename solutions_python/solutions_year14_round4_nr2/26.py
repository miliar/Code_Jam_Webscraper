import sys

(_stdin, sys.stdin) = (sys.stdin, open('B-large.in', 'r'))
(_stdout, sys.stdout) = (sys.stdout, open('B-large.out', 'w'))

T = int(input())

for t in range(1, T+1):
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    while A:
        k = 0
        for j in range(len(A)):
            if A[j] < A[k]:
                k = j
        ans += min(k, len(A)-1-k)
        del A[k]
    print('Case #%d: %d' % (t, ans))