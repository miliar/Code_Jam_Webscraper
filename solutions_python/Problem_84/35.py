def parse(f):
    rows = [r.strip() for r in open(f).read().split('\n')]
    num_cases = rows.pop(0)
    case = 1
    while True:
        x,y = rows.pop(0).split(' ')
        stuff = [list(rows.pop(0)) for i in xrange(int(x))]
        solve(stuff, case)
        case += 1


def solve(block, case):
    x = len(block[0])
    y = len(block)
    possible = True
    for i in xrange(y-1):
        for j in xrange(x-1):
            if all(b == '#' for b in [block[i][j], block[i+1][j], block[i][j+1], block[i+1][j+1]]):
                block[i][j] = '/'
                block[i+1][j] = '\\'
                block[i][j+1] = '\\'
                block[i+1][j+1] = '/'
    for r in block:
        for c in r:
            if c == '#':
                possible = False
    result = '\n' + ''.join(r for r in [''.join(b)+'\n' for b in block])
    if not possible:
        print 'Case #%d:\nImpossible' % case
    else:
        print 'Case #%d: %s' % (case, result)


f = 'A-large.in'
parse(f)
