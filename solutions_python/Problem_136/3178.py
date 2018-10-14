def solve(c, f, x):
    i = 0
    best = x / 2.0
    factory_cost = 0.0
    while True:
        factory_cost += c / (i * f + 2.0)
        total_cost = factory_cost + (x / ((i + 1) * f + 2.0))
        i += 1
        if total_cost < best:
            best = total_cost
        else:
            break
    return best


if __name__ == '__main__':
    T = int(raw_input())
    for t in xrange(T):
        c, f, x = map(float, raw_input().split())
        answer = solve(c, f, x)
        print 'Case #%d: %.7f' % (t + 1, answer)
