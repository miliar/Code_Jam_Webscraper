from __future__ import print_function
import sys

sin = '''6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
'''

def err(*msgs, **argv):
    print(*msgs, file=sys.stderr, **argv)

def solveCase(board):
    winner = None
    dotExists = False
    for i in range(4):
        row = findWinner(board[i])
        if not dotExists and '.' in board[i]:
            dotExists = True
        col = findWinner([board[r][i] for r in range(4)])
        if row or col:
            winner = row or col
    dia1 = findWinner([board[i][i] for i in range(4)])
    dia2 = findWinner([board[i][3-i] for i in range(4)])

    if dia1 or dia2:
        winner = dia1 or dia2

    if winner:
        return '%s won' % winner 
    elif dotExists:
        return 'Game has not completed'
    else:
        return 'Draw'



def findWinner(l):
    lst = list(l)
    if 'T' in lst:
        lst.remove('T')
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1] or lst[i] == '.':
            return None
    return lst[0] if lst[0] != 'T' else lst[1]



def solveAll(s):
    it = iter(s.split('\n'))
    T = int(it.next())
    for i in range(T):
        board = []
        for j in range(4):
            board.append(list(it.next()))
        #Empty line
        it.next()
        yield('Case #%s: %s' % (i + 1, solveCase(board)))


def test():
    err('\n'.join(solveAll(sin)))

if __name__ == '__main__':
    if not sys.argv[1:]:
        test()
        sys.exit(0)
    fn = sys.argv[1]
    print('\n'.join(solveAll(open(fn).read())))
