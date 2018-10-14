#!/usr/bin/env python3.5

def flip(happy, K):
    count = 0
    for i in range(len(happy) - K + 1):
        if happy[i] == 1:
            continue
        count += 1
        happy[i:i + K] = [x ^ 1 for x in happy[i:i + K]]
    if any(x == 0 for x in happy[-K + 1:]):
        return 'IMPOSSIBLE'
    else:
        return count


N = int(input())
m = {'-': 0, '+': 1}
for i in range(N):
    s, K = input().split()
    s = [m[x] for x in s]
    K = int(K)
    count = flip(s, K)
    print('Case #{}: {}'.format(i + 1, count))

