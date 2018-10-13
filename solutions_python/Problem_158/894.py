T = int(raw_input())

for case in xrange(T):

    X, R, C = map(int, raw_input().split())

    winner = None

    cells = R*C

    if cells % X != 0:
        winner = 'RICHARD'
    else:
        if X == 3:
            if cells >= 2*X:
                winner = 'GABRIEL'
            else:
                winner = 'RICHARD'
        elif X == 4:
            if cells >= 3*X:
                winner = 'GABRIEL'
            else:
                winner = 'RICHARD'
        else:
            if cells >= X:
                winner = 'GABRIEL'
            else:
                winner = 'RICHARD'


    print 'Case #%d: %s' % (case+1, winner)

