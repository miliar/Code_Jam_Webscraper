def parse_file(fnIn):
    assert fnIn.endswith('.in')
    fnOut = fnIn.replace('.in', '.out')

    with open(fnOut, 'w') as fOut:
        with open(fnIn, 'rU') as fIn:
            T = int(fIn.readline())

            for n in xrange(T):
                C,F,X = map(float, fIn.readline().split())

                t = time_for_optimal_strat(C, F, X)

                fOut.write('Case #%d: %.7f\n'%(n + 1, t))


COOKIES_PER_SEC = 2


def time_for_optimal_strat(C, F, X):
    t = 0

    c = 0
    dc = COOKIES_PER_SEC

    while 1:
        # We make a decision when we can afford a farm
        timeToFarm = (C - c)/dc

        t += timeToFarm
        c = C

        # Work out how long it would take to win immediately, or with the farm
        timeToWinImmediately = (X - c)/dc
        timeToWinWithFarm = X/(dc + F)

        # If we can win immediately, just do that
        if timeToWinImmediately <= timeToWinWithFarm:
            return t + timeToWinImmediately

        # Otherwise, buy the farm
        c -= C
        dc += F
