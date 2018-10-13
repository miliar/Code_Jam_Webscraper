from collections import defaultdict

def split_stalls(n):
    if n % 2 == 0:
        return ((n - 1) // 2, n // 2)
    return ((n - 1) // 2, (n - 1) // 2)

def solve(n, k):
    gaps = defaultdict(int)
    gaps[n] = 1
    while True:
        gap = max(gaps.keys())
        count = gaps.pop(gap)
        l, r = split_stalls(gap)
        gaps[l] += count
        gaps[r] += count
        if sum(gaps.values()) > k:
            return str(r) + ' ' + str(l)

t = int(input())
for j in range(t):
    print("Case #" + str(j + 1) + ":", end=' ')
    n, k = map(int, input().split())
    print(solve(n, k))