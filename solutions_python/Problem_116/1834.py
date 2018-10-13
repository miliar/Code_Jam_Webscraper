def status(a):
    for i in xrange(4):
        s = set(a[i])
        if s.issubset(set(['T', 'X'])):
            return 'X'
        elif s.issubset(set(['T', 'O'])):
            return 'O'
    for j in xrange(4):
        s = set([a[0][j], a[1][j], a[2][j], a[3][j]])
        if s.issubset(set(['T', 'X'])):
            return 'X'
        elif s.issubset(set(['T', 'O'])):
            return 'O'
    s = set([a[i][i] for i in xrange(4)])
    if s.issubset(set(['T', 'X'])):
        return 'X'
    elif s.issubset(set(['T', 'O'])):
        return 'O'
    s = set([a[i][4 - i - 1] for  i in xrange(4)])
    if s.issubset(set(['T', 'X'])):
        return 'X'
    elif s.issubset(set(['T', 'O'])):
        return 'O'
    for i in xrange(4):
        if '.' in a[i]:
            return 'nd'
    return 'd'

n = int(raw_input())

for i in xrange(n):
    a = []
    for j in xrange(4):
        a.append(list(raw_input()))
    raw_input()
    s = status(a)
    if s == 'X':
        print 'Case #%d: X won' % (i + 1)
    elif s == 'O':
        print 'Case #%d: O won' % (i + 1)
    elif s == 'nd':
        print 'Case #%d: Game has not completed' % (i + 1)
    else:
        print 'Case #%d: Draw' % (i + 1)
