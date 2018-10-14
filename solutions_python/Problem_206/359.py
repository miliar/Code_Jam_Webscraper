def solve(d, h):
    t = 0
    for k, s in h:
        if k >= 0:
            t = max(t, (d - k) / s)
    return d / t

for i in range(1, int(input())+1):
    print('Case #', i, ': ', solve(*(lambda a, b: (a, [tuple(map(int, input().split())) for i in range(b)]))(*map(int, input().split()))), sep='')
