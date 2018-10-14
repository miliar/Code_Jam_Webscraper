from math import pi


def iter(pcks, idx, prev, tot, count, k):
    if idx > len(pcks):
        return -1
    if count == k:
        return tot

    res1 = res2 = -1
    surf = pcks[idx][0] * pcks[idx][0]
    res1 = iter(pcks, idx + 1, surf, tot - prev + surf + 2 *
                pcks[idx][1] * pcks[idx][0], count + 1, k)
    if len(pcks) - idx > k - count:
        res2 = iter(pcks, idx + 1, prev, tot, count, k)
    return max(res1, res2)

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    pancakes = []
    for j in range(n):
        pancakes.append(list(map(int, input().split())))

    s_pancakes = sorted(pancakes, key=lambda x: x[0])
    res = iter(s_pancakes, 0, 0, 0, 0, k)

    print('Case #%d: %.9f' % (i + 1, res * pi))
