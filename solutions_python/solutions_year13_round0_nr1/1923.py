from sys import stdin
from pylab import asarray, logical_or, diag, rot90, any, all, ravel

def getProb():
    board = []
    for i in xrange(4):
        board.append(list(stdin.readline()[:-1]))
    stdin.readline()
    return asarray(board)

def solve(board):
    if win(board, 'X'):
        return 'X won'
    elif win(board, 'O'):
        return 'O won'
    elif draw(board):
        return 'Draw'
    else:
        return 'Game has not completed'

def win(board, letter):
    wins = logical_or(board == letter, board == 'T')
    return any(all(wins, 0)) or any(all(wins, 1)) or all(diag(wins)) or \
      all(diag(rot90(wins)))

def draw(board):
    return all(ravel(board != '.'))

if __name__ == '__main__':
    T = int(stdin.readline())
    for i in xrange(T):
        print 'Case #' + str(i + 1) + ':', solve(getProb())
