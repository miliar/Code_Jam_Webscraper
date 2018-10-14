f = open('1.in', 'r')
o = open('1.out', 'w')
T = int(f.readline().strip())


def solve():
    for t in xrange(T):
        m = [[x for j, x in enumerate(f.readline().strip())] for i in range(4)]

        p = c(m)
        f.readline()

        if p == 'O':
            res = 'O won'
        elif p == 'X':
            res = 'X won'
        elif p == 0:
            res = 'Draw'
        else:
            res = 'Game has not completed'
        s = "Case #%d: %s\n" % (t + 1, res)
        o.write(s)


def c(m):
    dot = 0
    for i in range(4):
        x, o = 0, 0
        for j in range(4):
            e = m[i][j]
            if e == 'X':
                x += 1
            elif e == 'O':
                o += 1
            elif e == '.':
                dot += 1
            else:
                x += 1
                o += 1
        if x == 4:
            return 'X'
        elif o == 4:
            return 'O'
    for i in range(4):
        x, o = 0, 0
        for j in range(4):
            e = m[j][i]
            if e == 'X':
                x += 1
            elif e == 'O':
                o += 1
            elif e == '.':
                dot += 1
            else:
                x += 1
                o += 1
        if x == 4:
            return 'X'
        elif o == 4:
            return 'O'
    x, o = 0, 0
    for i in range(4):
        e = m[i][i]
        if e == 'X':
            x += 1
        elif e == 'O':
            o += 1
        elif e == '.':
            dot += 1
        else:
            x += 1
            o += 1
    if x == 4:
        return 'X'
    elif o == 4:
        return 'O'
    x, o = 0, 0
    for i in range(4):
        e = m[i][3 - i]
        if e == 'X':
            x += 1
        elif e == 'O':
            o += 1
        elif e == '.':
            dot += 1
        else:
            x += 1
            o += 1
    if x == 4:
        return 'X'
    elif o == 4:
        return 'O'
    return dot

solve()
