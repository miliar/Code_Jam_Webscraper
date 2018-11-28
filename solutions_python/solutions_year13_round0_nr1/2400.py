s = open("i3")
t = open("output", "w")

def cond(row):
    if sum(1 for c in row if c in ('T', 'X')) == 4:
        return 'X'
    if sum(1 for c in row if c in ('T', 'O')) == 4:
        return 'O'
    if '.' in row:
        return 'empty'

def combs(board):
    for row in board:
        yield row
    for col in zip(*board):
        yield col
    yield [board[i][i] for i in range(4)]
    yield [board[i][3-i] for i in range(4)]

def check(board):
    isdraw = True
    for comb in combs(board):
        c = cond(comb)
        #        print c, comb
        if c == 'X':
            return 'X won'
        if c == 'O':
            return 'O won'
        if c == 'empty':
            isdraw = False
    return 'Draw' if isdraw else 'Game has not completed'

n = int(s.readline().strip())
for i in range(n):
    board = [s.readline().strip() for _ in range(4)]
    out = "Case #{}: {}".format(i+1, check(board))
    t.write(out + "\n")
    print(out)
    assert not s.readline().strip()
t.close()
