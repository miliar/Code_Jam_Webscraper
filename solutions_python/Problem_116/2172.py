def winner(field):
    transposed = zip(*field)
    blanks = 0
    
    for i in range(4):
        if field[i].count('X') == 4 or (field[i].count('X') == 3 and field[i].count('T') == 1):
            return 'X won'
        if field[i].count('O') == 4 or (field[i].count('O') == 3 and field[i].count('T') == 1):
            return 'O won'
        if transposed[i].count('X') == 4 or (transposed[i].count('X') == 3 and transposed[i].count('T') == 1):
            return 'X won'
        if transposed[i].count('O') == 4 or (transposed[i].count('O') == 3 and transposed[i].count('T') == 1):
            return 'O won'
        
        blanks += field[i].count('.');
    
    
    diag1 = [field[i][i] for i in range(4)]
    diag2 = [field[i][3 - i] for i in range(4)]
    
    if diag1.count('X') == 4 or (diag1.count('X') == 3 and diag1.count('T') == 1):
        return 'X won'
    if diag1.count('O') == 4 or (diag1.count('O') == 3 and diag1.count('T') == 1):
        return 'O won'
    
    if diag2.count('X') == 4 or (diag2.count('X') == 3 and diag2.count('T') == 1):
        return 'X won'
    if diag2.count('O') == 4 or (diag2.count('O') == 3 and diag2.count('T') == 1):
        return 'O won'
    
    if blanks == 0:
        return 'Draw'
    else:
        return 'Game has not completed'

def get_input():
    l = [list(raw_input()) for _ in range(5)]
    l.pop()
    return l
    
if __name__ == '__main__':
    n = int(raw_input())
    fields = [get_input() for _ in range(n)]
    for i in range(n):
        print "Case #%d: %s" % (i + 1, winner(fields[i]))
    
    
