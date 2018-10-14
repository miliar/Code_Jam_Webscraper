from collections import defaultdict


def solve(n, k):
    d = defaultdict(lambda: 0)
    d[n] = 1
    while True:
        old_items = list(reversed(sorted(d.items())))
        d = defaultdict(lambda: 0)
        for key, val in old_items:
            if k <= val:
                return key // 2, key // 2 - (key % 2 == 0)
            k -= val

            if key % 2 == 0:
                d[key // 2] += val
                d[key // 2 - 1] += val
            else:
                d[key // 2] += 2 * val


t = int(input())
for case in range(1, t + 1):
    n, k = map(int, input().split())
    print('Case #{}: {} {}'.format(case, *solve(n, k)))
