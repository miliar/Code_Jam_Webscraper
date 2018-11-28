def isIt(X, R, C):
    if X == 1:
        return 'GABRIEL'
    if X == 2:
        t = [(1, 1), (1, 3), (3, 3)]
        if (R, C) in t or (C, R) in t:
            return 'RICHARD'
        return 'GABRIEL'
    if X == 3:
        t = [(2, 3), (3, 4), (3, 3)]
        if (R, C) in t or (C, R) in t:
            return 'GABRIEL'
        return 'RICHARD'
    if X == 4:
        t = [(3, 4), (4, 4)]
        if (R, C) in t or (C, R) in t:
            return 'GABRIEL'
        return 'RICHARD'


for i in range(input()):
    X, R, C = map(int, raw_input().split())
    print 'Case #' + str(i+1) + ': ' + isIt(X, R, C)
