string = [s.strip() for s in
          open('input1.txt').readlines()[1:] if len(s.strip())]


def get_chunk():
    res = []
    for index, line in enumerate(string):
        res.append(line)
        if len(res) == 4:
            yield res
            res = []

    if res:
        yield res


def solve(chunk):
    dot_found = False
    # vertical check
    for i in xrange(4):
        found = True
        mark = chunk[1][i] if chunk[0][i] == 'T' else chunk[0][i]
        if mark == '.':
            dot_found = True
            continue
        for j in xrange(1, 4):
            if chunk[j][i] == '.':
                dot_found = True
            if chunk[j][i] != mark and chunk[j][i] != 'T':
                found = False
        if found:
            # print 'vert', i
            return mark + ' won'
    # horz check
    for i in xrange(4):
        found = True
        mark = chunk[i][1] if chunk[i][0] == 'T' else chunk[i][0]
        if mark == '.':
            dot_found = True
            continue
        for j in xrange(1, 4):
            if chunk[i][j] == '.':
                dot_found = True
            if chunk[i][j] != mark and chunk[i][j] != 'T':
                found = False
        if found:
            # print 'horz', i
            return mark + ' won'
    # desc diag check
    mark = chunk[1][1] if chunk[0][0] == 'T' else chunk[0][0]
    if mark != '.':
        found = True
        for i in xrange(1, 4):
            if chunk[i][i] != mark and chunk[i][i] != 'T':
                found = False
                break
        if found:
            # print 'desc'
            return mark + ' won'
    # asc diag check
    mark = chunk[2][1] if chunk[3][0] == 'T' else chunk[3][0]
    if mark != '.':
        found = True
        for i in xrange(2, -1, -1):
            if chunk[i][3 - i] != mark and chunk[i][3 - i] != 'T':
                found = False
                break
        if found:
            # print 'asc'
            return mark + ' won'
    if dot_found:
        return 'Game has not completed'
    else:
        return 'Draw'

for index, chunk in enumerate(get_chunk()):
    print 'Case #%s:' % (index + 1), solve(chunk)
    # break
