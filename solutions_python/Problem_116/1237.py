# encoding: utf-8

def now():
    f = open('A-large.in')
    n = int(f.readline().strip())

    for t in range(n):
        has_dot = False
        lines = []
        for i in range(4):
            lines.append(f.readline().strip())
            if '.' in lines[i]:
                has_dot = True
        f.readline()
        
        for j in range(4):
            line = []
            for k in range(4):
                line.append(lines[k][j])
            lines.append(line)
        line = []
        line.append(lines[0][0])
        line.append(lines[1][1])
        line.append(lines[2][2])
        line.append(lines[3][3])
        lines.append(line)

        line = []
        line.append(lines[0][3])
        line.append(lines[1][2])
        line.append(lines[2][1])
        line.append(lines[3][0])
        lines.append(line)

#         print lines
        ch = check(lines)
        if ch != 'N':
            print 'Case #%d: %s won' % ((t + 1), ch)
        elif has_dot:
            print 'Case #%d: Game has not completed' % (t + 1)
        else:
            print 'Case #%d: Draw' % (t + 1)


def check(lines):
    for i in lines:
        ch = check_row(i)
        if ch != 'N':
            return ch
    return 'N'

def check_row(row):
    if row.count('X') == 4 or \
            (row.count('X') == 3 and 'T' in row):
        return 'X'
    if row.count('O') == 4 or \
            (row.count('O') == 3 and 'T' in row):
        return 'O'
    return 'N'


if __name__ == '__main__':
    import sys
    old = sys.stdout
    sys.stdout = open('out.txt', 'w')
    now()
    sys.stdout = old


