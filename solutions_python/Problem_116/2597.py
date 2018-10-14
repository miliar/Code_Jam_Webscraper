table = {
    '.': 0, 'T': 3, 'X': 1, 'O': 2
}

H  = 0b01010101
V  = 0b00000001000000010000000100000001
C1 = 0b01000000000100000000010000000001
C2 = 0b00000001000001000001000001000000


def read_test_case(f):
    c = 0
    d = 0
    for i in range(4):
        x = f.readline()
        for j, y in enumerate(x[:-1]):
            c = c | (table[y] << (j * 2 + i * 8))
            if table[y] == 0:
                d += 1
    return c, d


def check_win(c, shift):
    for i in range(4):
        if (c & (H << (i * 8 + shift))) == (H << (i * 8 + shift)):
            return True
    for i in range(4):
        if (c & (V << (i * 2 + shift))) == (V << (i * 2 + shift)):
            return True
    for y in (C1, C2):
        if (c & (y << shift)) == (y << shift):
            return True
    return False

o = open('out.txt', 'w')
with open('test.txt', 'r') as g:
    u = int(g.readline().strip())
    for k in range(u):
        o.write('Case #{0}: '.format(k + 1))

        c, d = read_test_case(g)
        g.readline()
        owon = check_win(c, 1)
        xwon = check_win(c, 0)
        if not (owon or xwon):
            if d == 0:
                o.write('Draw\n')
            else:
                o.write('Game has not completed\n')
        elif owon:
            o.write('O won\n')
        elif xwon:
            o.write('X won\n')
