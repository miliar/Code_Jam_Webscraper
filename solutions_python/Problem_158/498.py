def getWinner(X, R, C):
    gab = "GABRIEL"
    rich = "RICHARD"
    if X == 1:
        return gab
    def _f(x, y):
        if x == 1:
            if y == 2:
                if X == 2:
                    return gab
            if y == 4:
                if X == 2:
                    return gab
            return rich
        if x == 2:
            if y == 2:
                if X == 2:
                    return gab
            if y == 3:
                if X == 2:
                    return gab
                if X == 3:
                    return gab
            if y == 4:
                if X == 2:
                    return gab
            return rich
        if x == 3:
            if y == 3:
                if X == 2:
                    return rich
                if X == 3:
                    return gab
                return rich
            if y == 4:
                if X <= 4:
                    return gab
                return rich
            return rich
        if x == 4:
            if y == 4:
                if X == 2:
                    return gab
                if X == 3:
                    return rich
                if X == 4:
                    return gab
        return rich

    if R < C:
        return _f(R, C)
    return _f(C, R)


def test():
    assert getWinner(2, 2, 2) == 'GABRIEL'
    assert getWinner(2, 1, 3) == 'RICHARD'
    assert getWinner(4, 4, 1) == 'RICHARD'
    assert getWinner(3, 2, 3) == 'GABRIEL'

if __name__ == '__main__':
    test()
    import sys
    with sys.stdin as f:
        T = int(f.readline())
        for i in range(1, T+1):
            X, R, C = [int(j) for j in f.readline().split()]
            print "Case #%d: %s" % (i, getWinner(X, R, C))
