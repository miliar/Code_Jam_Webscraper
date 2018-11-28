import sys

def dec(d, c, x):
    if c in d:
        d[c] -= x

def solve(s):
    # TODO Solve the problem
    table = dict()

    for c in s:
        if c in table:
            table[c] += 1
        else:
            table[c] = 1

    rv = ''
    cnt = [0] * 10

    if 'Z' in table:
        cnt[0] = table['Z']

        dec(table, 'E', table['Z'])
        dec(table, 'R', table['Z'])
        dec(table, 'O', table['Z'])

        table['Z'] = 0

    if 'W' in table:
        cnt[2] = table['W']

        dec(table, 'T', table['W'])
        dec(table, 'O', table['W'])

        table['W'] = 0

    if 'U' in table:
        cnt[4] = table['U']

        dec(table, 'F', table['U'])
        dec(table, 'O', table['U'])
        dec(table, 'R', table['U'])

        table['U'] = 0

    if 'X' in table:
        cnt[6] = table['X']

        dec(table, 'S', table['X'])
        dec(table, 'I', table['X'])

        table['X'] = 0

    if 'G' in table:
        cnt[8] = table['G']

        dec(table, 'E', table['G'])
        dec(table, 'I', table['G'])
        dec(table, 'H', table['G'])
        dec(table, 'T', table['G'])

        table['G'] = 0

    if 'O' in table:
        cnt[1] = table['O']

        dec(table, 'N', table['O'])
        dec(table, 'E', table['O'])

        table['O'] = 0

    if 'R' in table:
        cnt[3] = table['R']

        dec(table, 'T', table['R'])
        dec(table, 'H', table['R'])
        dec(table, 'E', 2 * table['R'])

        table['R'] = 0

    if 'F' in table:
        cnt[5] = table['F']

        dec(table, 'I', table['F'])
        dec(table, 'V', table['F'])
        dec(table, 'E', 2 * table['F'])

        table['F'] = 0

    if 'S' in table:
        cnt[7] = table['S']

        dec(table, 'E', 2 * table['S'])
        dec(table, 'V', table['S'])
        dec(table, 'N', 2 * table['S'])

        table['S'] = 0

    if 'I' in table:
        cnt[9] = table['I']

    for i in range(10):
        if cnt[i] > 0:
            rv += str(i) * cnt[i]

    return rv

### Convert the input file into a list of strings ###
in_file = sys.argv[1]

with open(in_file, "r") as f:
    data = f.read()

lines = data.splitlines()
### Convert the input file into a list of strings ###

### Interpret the arguments ###
cases = int(lines.pop(0))

for i in range(1, cases + 1):
    s = lines.pop(0)

    answer = solve(s)

    print 'Case #%d: %s' % (i, answer)
### Interpret the arguments ###
