def row(a, i, j, di, dj, player):
    for _ in xrange(4):
        if i < 0 or i >= 4 or j < 0 or j >= 4:
            return False
        if a[i][j] not in [player, 'T']:
            return False
        i += di
        j += dj
    return True


def won(a, player):
    for i in xrange(4):
        for j in xrange(4):
            for di, dj in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                if row(a, i, j, di, dj, player):
                    return True
    return False


def draw(a):
    for r in a:
        for c in r:
            if c == '.':
                return False
    return True


cases = input()
for test in xrange(1, cases + 1):
    a = []
    for _ in xrange(4):
        a.append(raw_input())
    raw_input()
    result = None
    if won(a, 'X'):
        result = 'X won'
    elif won(a, 'O'):
        result = 'O won'
    elif draw(a):
        result = 'Draw'
    else:
        result = 'Game has not completed'
    print 'Case #{}: {}'.format(test, result)
