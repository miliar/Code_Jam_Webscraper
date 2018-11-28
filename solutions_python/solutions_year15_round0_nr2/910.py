import os


inp = open('b.in').readlines()
t = int(inp[0])
prec = {}


def solve(cnt, pancakes):
    global prec
    if max(pancakes) == 1:
        return cnt + 1

    if str(pancakes) in prec:
        return cnt + prec[str(pancakes)]

    res = max(pancakes)
    if pancakes[0] >= 4:
        for sp in range(2, pancakes[0]):
            new_ps = [pancakes[0] - sp, sp] + pancakes[1:]
            new_ps.sort(reverse=True)

            res = min(res, solve(cnt + 1, new_ps) - cnt)

    prec[str(pancakes)] = res
    return res + cnt

for idx in range(t):
    pancakes = [int(c) for c in inp[idx*2 + 2].split(' ')]
    pancakes.sort(reverse=True)
    print('Case #%d: %d' % (idx + 1, solve(0, pancakes)))