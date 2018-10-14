def solve(s):
    a, r = 0, 0
    for i, v in enumerate(s[:-1]):
        a += int(v)
        t = i + 1 - a
        if t > 0:
            r += t
            a += t
    return r

with open('input/alarge.in') as f:
    n = int(f.readline())
    for i in range(n):
        s = f.readline().split(' ')[1]
        print('Case #{}: {}'.format(i + 1, solve(s)))
