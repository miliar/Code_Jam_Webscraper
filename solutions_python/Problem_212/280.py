def solve(n, p, gs):
    xs = [0] * p
    for x in gs:
        xs[x%p] += 1
    if p == 2:
        return n - xs[1] // 2
    if p == 3:
        m = min(xs[1], xs[2])
        M = max(xs[1], xs[2])
        return xs[0] + m + (M - m + 2) // 3
    if p == 4:
        m = min(xs[1], xs[3])
        M = max(xs[1], xs[3])
        return xs[0] + xs[2] // 2 - m - (M - m) - xs[2] // 2 + 1

for i in range(input()):
    [n, p] = map(int, raw_input().split())
    gs = map(int, raw_input().split())
    print 'Case #{}: {}'.format(i+1, solve(n, p, gs))
