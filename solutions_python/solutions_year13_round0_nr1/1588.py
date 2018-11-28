f_in = open('tttt.in')
f_out = open('tttt.out', 'w')

count = int(f_in.readline())


def check(rows):
    inc = False

    for row_num in xrange(4):
        line = rows[row_num]

        print line

        first = ''

        col = 0
        while col < 4:
            if line[col] == '.':
                inc = True
                print('Row %d is incomplete' % row_num)
                break

            if not first:
                if line[col] != 'T':
                    first = line[col]
                    print('First: ' + first)
            else:
                if line[col] not in [first, 'T']:
                    print('Mismatch on col %d' % col)
                    break

            col += 1

        if col == 4:
            return first + ' won'

    for col in xrange(4):
        first = ''

        row = 0
        while row < 4:
            if rows[row][col] == '.':
                print('Col %d is incomplete' % col)
                break

            if not first:
                if rows[row][col] != 'T':
                    first = rows[row][col]
                    print('First: ' + first)
            else:
                if rows[row][col] not in [first, 'T']:
                    print('Mismatch on row %d' % row)
                    break

            row += 1

        if row == 4:
            return first + ' won'

    first = ''

    i = 0
    while i < 4:
        if rows[i][i] == '.':
            print('%d is incomplete' % i)
            break

        if not first:
            if rows[i][i] != 'T':
                first = rows[i][i]
                print('First: ' + first)
        else:
            if rows[i][i] not in [first, 'T']:
                print('Mismatch on %d' % i)
                break

        i += 1

    if i == 4:
        return first + ' won'

    first = ''

    i = 0
    while i < 4:
        if rows[i][3-i] == '.':
            print('%d is incomplete' % i)
            break

        if not first:
            if rows[i][3-i] != 'T':
                first = rows[i][3-i]
                print('First: ' + first)
        else:
            if rows[i][3-i] not in [first, 'T']:
                print('Mismatch on %d' % i)
                break

        i += 1

    if i == 4:
        return first + ' won'

    if inc:
        return 'Game has not completed'

    return 'Draw'


for case in range(1, count + 1):
    print('Case #%d:' % case)

    rows = {}
    for i in xrange(4):
        rows[i] = f_in.readline().strip()

    result = check(rows)

    print(result)

    f_in.readline()

    f_out.write('Case #%d: %s\n' % (case, result))
