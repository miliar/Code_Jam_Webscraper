def wins_omino(x, r, c):
    if x == 1:
        return 'GABRIEL'
    if x == 2:
        return 'GABRIEL' if r*c % x == 0 else 'RICHARD'
    if x == 3:
        if r > 1 and c > 1:
            if r*c % x == 0:
                return 'GABRIEL'
        return 'RICHARD'
    if x == 4:
        if r*c % x == 0 and r > 2 and c > 2:
            return 'GABRIEL'
        else:
            return 'RICHARD'

cases = [(2, 2, 2),
         (2, 1, 3),
         (4, 4, 1),
         (3, 2, 3)]

t = input()
for i in range(t):
    x, r, c = map(int, raw_input().split())
    # x, r, c = cases[i]
    result = wins_omino(x, r, c)
    print "Case #%d: %s" % (i+1, result)
