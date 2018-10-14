import sys
import collections

def read_board():
    board = ''
    for line in range(4):
        board += input()
    return board

def rows(board):
    return [board[:4],board[4:8],board[8:12],board[12:16]]

def cols(board):
    ans = []
    for idx in range(4):
        segment = ''
        for delta in range(0,16,4):
            segment += board[idx+delta]
        ans.append(segment)
    return ans

def diag(board):
    d = ''.join([board[i] for i in (0,5,10,15)])
    a = ''.join([board[i] for i in (3,6,9,12)])
    return [d,a]

def status(board):
    xw = 'X won'
    ow = 'O won'
    x,o,t = 'X','O','T'
    # rows
    for segment in rows(board)+diag(board)+cols(board):
        count = collections.defaultdict(int)
        for c in segment:
            count[c] +=1
        if count[x]+count[t] == 4:
            return xw
        elif count[o]+count[t] == 4:
            return ow

    return 'Game has not completed' if '.' in board else 'Draw'

if __name__ == '__main__':
    T = int(input())
    case = 1
    while case <= T:
        if case != 1: input()
        board = read_board()
        print('Case #{}: {}'.format(case, status(board)))
        case += 1
