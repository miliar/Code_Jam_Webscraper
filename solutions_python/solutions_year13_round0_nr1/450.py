import itertools, os

def column(mat, n):
    return [row[n] for row in mat]

def columns(mat):
    return (column(mat, n) for n in xrange(len(mat[0]))) if mat else ()

def rows(mat):
    return (list(m) for m in mat)

def check(board):
    for player in ('X','O'):
        diagonals = (
            [board[0][0], board[1][1], board[2][2], board[3][3]],
            [board[0][3], board[1][2], board[2][1], board[3][0]]
        )
        for line in itertools.chain(rows(board), columns(board), diagonals):
            if all(ch in (player,'T') for ch in line):
                return player

def main():
    inpath = 'A-large.in'
    outpath = os.path.splitext(inpath)[0] + '.out'
    with open(inpath,'r') as infile, open(outpath,'w') as outfile:
        T = int(infile.readline())
        for t in xrange(T):
            board = []

            for line in xrange(4):
                board.append(infile.readline().rstrip())

            winner = check(board)

            outfile.write('Case #%d: ' % (t+1))
            if winner:
                outfile.write('%s won\n' % winner)
            elif any(ch=='.' for ch in itertools.chain(*board)):
                outfile.write('Game has not completed\n')
            else:
                outfile.write('Draw\n')

            infile.readline() # discard blank line between games

if __name__ == '__main__':
    main()
