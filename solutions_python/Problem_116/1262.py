#Tic-Tac-Toe-Tomek
import sys

def check(board, win):
    for i in xrange(4):
        if board[i] == win:
            return True
    for j in xrange(4):
        y = "".join([x[j] for x in board])
        if y == win:
            return True
    y = "".join([board[i][i] for i in xrange(4)])
    if y == win:
        return True
    y = "".join([board[i][3 - i] for i in xrange(4)])
    if y == win:
        return True
    return False

if __name__ == "__main__":
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')

    T = int(infile.readline().strip())
    for num in xrange(1, T+1):
        board = []
        for i in xrange(4):
            line = infile.readline().strip()
            board.append(line)
        infile.readline()

        Xb = board[:]
        for i in xrange(4):
            Xb[i] = Xb[i].replace('T', 'X')
        if check(Xb, 'XXXX'):
            print >> outfile, 'Case #%d: X won' % num
            continue

        Ob = board[:]
        for i in xrange(4):
            Ob[i] = Ob[i].replace('T', 'O')
        if check(Ob, 'OOOO'):
            print >> outfile, 'Case #%d: O won' % num
            continue

        res = 'Draw'
        for i in xrange(4):
            if '.' in board[i]:
                res = 'Game has not completed'
        print >> outfile, 'Case #%d: %s' % (num, res)
    infile.close()
    outfile.close()

