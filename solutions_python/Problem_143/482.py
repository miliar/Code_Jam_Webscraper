import sys

def solve(A, B, K):
    count = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                count += 1
    return count

T = int(sys.stdin.readline())
for i in range(1, T+1):
    A, B, K = tuple(map(int, sys.stdin.readline().strip().split(' ')))
    print "Case #{0}: {1}".format(i, solve(A, B, K))
