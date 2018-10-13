import fractions

def check_won(seq):
    if seq.replace('T', 'X').count('X') == 4:
        return "X won"
    if seq.replace('T', 'O').count('O') == 4:
        return "O won"
    return None

def solve():
    board = []
    for i in xrange(4):
        board.append(raw_input())
    raw_input()
    for i in xrange(4):
        ans = check_won(board[i])
        if ans != None:
            return ans
    for i in xrange(4):
        ans = check_won(''.join([board[j][i] for j in xrange(4)]))
        if ans != None:
            return ans
    ans = check_won(''.join([board[i][i] for i in xrange(4)]))
    if ans != None:
        return ans
    ans = check_won(''.join([board[3 - i][i] for i in xrange(4)]))
    if ans != None:
        return ans
    for i in xrange(4):
        if '.' in board[i]:
            return "Game has not completed"
    return "Draw"

T = int(raw_input())
for i in xrange(T):
    print "Case #%d:" % (i + 1), solve()
