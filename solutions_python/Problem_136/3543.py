def solve(c, f, x):
    if x <= c:
        return x / 2.0
    acc = 0.0
    t = x / 2.0
    r = 2.0
    while True:
        acc += c / r
        r += f
        tt = acc + x / r
        if t - tt < 1e-7:
            return t
        if tt < t:
            t = tt

def solve2(c, f, x):
    if x <= c:
        return x / 2.0
    t = x / 2.0
    r = 2.0
    while True:
        delta = x/(r + f) - (x - c)/r
        if delta < 0:
            return t
        t += delta
        r += f

def main():
    T = int(raw_input())
    for t in range(T):
        C, F, X = [float(a) for a in raw_input().split(' ')]
        solution = solve(C, F, X)
        print 'Case #%d: %.7f' % (t+1, solution)

main()
