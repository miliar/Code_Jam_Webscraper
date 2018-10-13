def solve(line, ch):
    c = line.count(ch)
    t = line.count('T')
    return c + t == 4 and c >= 3
t = input()
for cas in range(t):
    if cas : 
        raw_input()
    board = [raw_input() for i in range(4)]
    data = board  + map(''.join, zip(*board)) + \
        [''.join([board[i][i] for i in range(4)])] + \
        [''.join([board[3 - i][i] for i in range(4)])]
    total = ''.join(board)
    if any([solve(line, 'X') for line in data]):
        print 'Case #%d: %s won' %(cas + 1, 'X')
    elif any([solve(line, 'O') for line in data]):
        print 'Case #%d: %s won' %(cas + 1, 'O')
    elif total.count('X') + total.count('O') + total.count('T') == 16:
        print 'Case #%d: Draw' %(cas + 1)
    else:
        print 'Case #%d: Game has not completed' %(cas + 1)
