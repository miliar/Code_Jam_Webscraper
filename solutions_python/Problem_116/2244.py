import sys

def main():
    _, input_fn = sys.argv
    input = open(input_fn)
    cases = int(input.readline())
    def rl():

        return input.readline().strip("\n")
    for i in range(cases):
        board = (rl(), rl(), rl(), rl())
        for line in board:
            line.strip("\n")
        input.readline()  # empty line
        result = evaluate(board)
        print "Case #%i: %s" % (i+1, result)

def win(s):
    if '.' in s:
        return None
    if 'O' in s and 'X' in s:
        return None
    if 'X' in s:
        return 'X won'
    else:
        return 'O won'

def diag1(board):
    s = set()
    for i in range(4):
        s.add(board[i][i])
    yield s

def diag2(board):
    s = set()
    for i in range(4):
        s.add(board[i][4 - 1 - i])
    yield s

def rows(board):
    for row in board:
        yield set(row)

def cols(board):
    for col in zip(*board):
        yield set(col)

b = ('1234', '5678', 'abcd', 'efgh')

def evaluate(board):
    for r in rows(board):
        w = win(r)
        if w:
            return w
    for c in cols(board):
        w = win(c)
        if w:
            return w
    for d in diag2(board):
        w = win(d)
        if w:
            return w
    for d in diag1(board):
        w = win(d)
        if w:
            return w
    all = set()
    for row in board:
        for mark in row:
            all.add(mark)
    if '.' in all:
        return "Game has not completed"
    else:
        return "Draw"
        
main()
