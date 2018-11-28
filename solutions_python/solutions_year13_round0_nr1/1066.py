import sys


def merge(a, b):
    for k in a.keys():
        a[k] += b[k]


def msg(pos, s):
    print('Case #{0}: {1}'.format(pos, s))


def win(st):
    if st['X'] + st['T'] == 4:
        return 'X won'
    if st['O'] + st['T'] == 4:
        return 'O won'
    return None


def solve_table(pos, table):
    tst = {'X': 0, 'O': 0, 'T': 0, '.': 0}
    diag = {'X': 0, 'O': 0, 'T': 0, '.': 0}
    adiag = {'X': 0, 'O': 0, 'T': 0, '.': 0}

    for row in range(4):
        st = {'X': 0, 'O': 0, 'T': 0, '.': 0}
        for col in range(4):
            x = table[row][col]
            st[x] += 1
            if x == '.':
                break

        r = win(st)
        if r:
            return msg(pos, r)
        merge(tst, st)

        x = table[row][row]
        y = table[3 - row][row]
        diag[x] += 1
        adiag[y] += 1

    r = win(diag)
    if r:
        return msg(pos, r)
    r = win(adiag)
    if r:
        return msg(pos, r)

    for row in range(4):
        st = {'X': 0, 'O': 0, 'T': 0, '.': 0}
        for col in range(4):
            x = table[col][row]
            st[x] += 1
            if x == '.':
                break

        if st['X'] + st['T'] == 4:
            return msg(pos, 'X won')
        if st['O'] + st['T'] == 4:
            return msg(pos, 'O won')
        #merge(tst, st)

    if tst['.'] == 0:
        return msg(pos, 'Draw')

    return msg(pos, 'Game has not completed')


def solve(filename):
    with open(filename) as f:
        N = int(f.readline().strip())

        for i in range(N):
            table = []
            for j in range(4):
                table.append(f.readline().strip())
            f.readline()
            #print(table)
            solve_table(i + 1, table)


if __name__ == '__main__':
    solve(sys.argv[1])
