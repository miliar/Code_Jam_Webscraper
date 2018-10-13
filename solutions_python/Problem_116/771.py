def solve(board):
    data = board[:]
    for j in xrange(4):
        data.append(''.join(row[j] for row in board))
    data.append(''.join(board[j][j] for j in xrange(4)))
    data.append(''.join(board[j][3-j] for j in xrange(4)))
    for p in ['O','X']:
        for d in data:
            if d.replace(p, 'T') == 'TTTT':
                return "%s won" % p

    if any(cell=='.' for row in board for cell in row):
        return "Game has not completed"

    return "Draw"

if __name__ == '__main__':
    import sys
    l = [x.strip() for x in open(sys.argv[1]).readlines()[1:]]
    n = len(l) / 5
    for i in xrange(n):
        print "Case #%s: %s" % (i + 1, solve(l[i*5:(i+1)*5-1]))
