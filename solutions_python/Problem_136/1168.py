def solve(C, F, X):
    cps = 2.0
    t = 0
    while True:
        t_no_farm = X / cps
        t_farm = (C / cps) + (X / (cps + F))
        #print 't', t, 't_no_farm', t_no_farm, 't_farm', t_farm
        if t_farm < t_no_farm:
            t += (C / cps)
            cps += F
        else:
            return '%.8f' % (t + t_no_farm)


def run():
    T = int(raw_input())
    for i in xrange(T):
        C, F, X = [float(x) for x in raw_input().split()]
        r = solve(C, F, X)
        print 'Case #%d:' % (i + 1), r


if __name__ == '__main__':
    run()
