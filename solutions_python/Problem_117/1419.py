import sys

def valid_cut(board, n, m):
    for row in xrange(n):
        d = {} # maps elevations to their columns
        for col in xrange(m):
            e = board[row][col]
            if e in d:
                d[e].append(col)
            else:
                d[e] = [col]
                
        if len(d) != 1:
            for elev in d:
                if elev != max(d):
                    for e_col in d[elev]:
                        for e_row in xrange(n):
                            if board[e_row][e_col] > elev:
                                return False
    return True                       
f = open(sys.argv[1], 'r')

num_tests = int(f.readline())
case = 1

while case <= num_tests:
    n, m = map(int, f.readline().split(' '))
    board = []
    for i in xrange(n):
        board.append(map(int, f.readline().split(' ')))
    
    result = 'YES' if valid_cut(board, n, m) else 'NO'
            
    print 'Case #' + str(case) + ': ' + result
    case += 1