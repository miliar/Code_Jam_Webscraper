rd = input

def ints():
    return list(map(int, rd().split()))

def solve(ac, aj):
    if ac and aj: return 2
    xs = ac or aj
    if len(xs) == 1: return 2
    t, T = sorted(xs)
    m = max(T[0]-t[1], 1440 - T[1] + t[0])
    return 2 if m >= 720 else 4

for t in range(int(rd())):
    c, j = ints()
    print('Case #{}: {}'.format(
        t+1,
        solve([ints() for _ in range(c)],
              [ints() for _ in range(j)])))
