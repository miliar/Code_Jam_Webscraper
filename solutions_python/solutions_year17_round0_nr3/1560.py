import sys
import heapq
sys.stdout = open('c2.out', 'w')
sys.stdin  = open("c2.in", 'r')
T = int(raw_input())


def tidy(N):
    s = str(N)
    return list(s) == sorted(list(s))

def algorithm(N, K):
    ht = [0] * (N + 1)
    ht[N] = 1
    i = N
    while K > 0:
        while ht[i] == 0:
            i -= 1
            if i == 0:
                return "0 0"
        l = (i - 1) // 2
        r = i - 1 - l
        ht[l] += 1
        ht[r] += 1
        ht[i] -= 1
        K -= 1
        if K == 0:
            a, b = min(l, r), max(l, r)
            return str(b) + " " + str(a)

def solve():
    N, K = map(int, raw_input().split())
    return algorithm(N, K)

for i in range(1, T + 1):
    ans = solve()
    print "Case #" + str(i) + ": " + str(ans)