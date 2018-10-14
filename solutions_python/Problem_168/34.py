rl = raw_input
t = int(rl())

def first_and_last(seq):
    first = last = -1
    for i in xrange(len(seq)):
        if seq[i] != '.':
            last = i
            if first == -1:
                first = i
    return first, last

for cc in xrange(t):
    r, c = map(int, rl().split())
    board = [rl().strip() for i in xrange(r)]
    can = [[set(list('<>^v')) for j in xrange(c)]
           for i in xrange(r)]
    cnt = 0
    for i in xrange(r):
        row = board[i]
        c1, c2 = first_and_last(row)
        if c1 == -1: continue
        can[i][c1].remove('<')
        can[i][c2].remove('>')
    for j in xrange(c):
        col = [board[i][j] for i in xrange(r)]
        r1, r2 = first_and_last(col)
        if r1 == -1: continue
        can[r1][j].remove('^')
        can[r2][j].remove('v')

    cnt = 0
    possible = True

    for i in xrange(r):
        for j in xrange(c):
            if board[i][j] != '.':
                if board[i][j] not in can[i][j]:
                    cnt += 1
                if not can[i][j]:
                    possible = False

    print 'Case #%d:' % (cc+1),
    if not possible:
        print 'IMPOSSIBLE'
    else:
        print cnt
