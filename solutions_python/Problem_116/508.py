
def read_board(f):
    b = [f.readline().strip() for i in range(0,4)]
    f.readline()
    return b

def check(r):
    if '.' in r: 
        return None
    if 'X' in r and 'O' in r:
        return None
    if 'X' in r:
        return 'X won'
    if 'O' in r:
        return 'O won'
    return None
    

def solve_board(b):
    # rows
    for r in b:
        z = check(r)
        if not z is None:
            return z
    for c in range(0,4):
        r = b[0][c] + b[1][c] + b[2][c] + b[3][c]
        z = check(r)
        if not z is None:
            return z
    z = check(b[0][0] + b[1][1] + b[2][2] + b[3][3])
    if not z is None:
        return z
    z = check(b[3][0] + b[2][1] + b[1][2] + b[0][3])
    if not z is None:
        return z
    
    if '.' in b[0] or '.' in b[1] or '.' in b[2] or '.' in b[3]:
        return "Game has not completed"
    else:
        return "Draw"
    
def main(f):
    count = int(f.readline())

    for i in range(1, count+1):
        print 'Case #%d: %s' % (i, solve_board(read_board(f)))
    
import sys

if __name__ == '__main__':
    main(sys.stdin)
