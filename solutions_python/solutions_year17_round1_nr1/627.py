def ratatuj(input):
    lines = input.split('\n')
    cases = int(lines.pop(0))
    for case in range(cases):
        cake = []
        for i in range(int(lines.pop(0).split(' ')[0])):
            cake.append(list(lines.pop(0)))

        print 'Case #%d: %s' % (case+1, '\n' + '\n'.join([''.join(x) for x in solve(cake)]))


def solve(cake):
    for row in cake:
        c = row.count('?')
        if c == 0:
            pass
        elif c == len(row):
            pass
        else:
            letter = '?'
            for i in range(len(row)):
                if row[i] != '?':
                    letter = row[i]
                else:
                    row[i] = letter
            letter = '?'
            for i in reversed(range(len(row))):
                if row[i] != '?':
                    letter = row[i]
                else:
                    row[i] = letter

    row = ['?' for x in cake[0]]
    for i in range(len(cake)):
        if cake[i][0] == '?':
            cake[i] = row
        else:
            row = cake[i]

    row = ['?' for x in cake[0]]
    for i in reversed(range(len(cake))):
        if cake[i][0] == '?':
            cake[i] = row
        else:
            row = cake[i]

    return cake


ratatuj(input)