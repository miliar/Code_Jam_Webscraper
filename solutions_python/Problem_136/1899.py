def solve(C, F, X, capacity):
    best = 1e9
    t = 0
    while True:
        total = t + X / capacity
        if total < best:
            best = total
        else:
            break

        t += C / capacity
        capacity += F

    return best

if __name__ == '__main__':
    for caseno in xrange(int(raw_input())):
        C, F, X = [float(s) for s in raw_input().split()]
        sol = solve(C, F, X, 2.0)
        print 'Case #%d: %.7f' % (caseno + 1, sol)
