from collections import defaultdict
import itertools
import sys

def check(R, C, l):
    '''
    1 denotes a mine, 0 denotes it's NOT mine
    '''
    board = defaultdict(lambda: defaultdict(int))
    for i in range(R):
        board[i+2] = dict(enumerate(l[i], 2))
        board[i+2][0], board[i+2][1], board[i+2][C+2], board[i+2][C+3] = [0] * 4
    board[0], board[1], board[R+2], board[R+3] = [[0] * (C+4)] * 4
    clicks = []
    for i in range(2, R+2):
        for j in range(2, C+2):
            if board[i][j] == 1:
                continue
            neighbours = []
            for x_diff in range(-1, 2):
                for y_diff in range(-1, 2):
                    neighbours.append(board[i+x_diff][j+y_diff])
            if sum(neighbours) == 0:
                clicks.append((i, j))
    if len(clicks) == 0:
        return []
    clicks_set = set(clicks)
    for i, j in clicks:
        neighbours = set([(i+d1, j+d2) for d1 in range(-1, 2) for d2 in range(-1, 2)])
        if len(neighbours & clicks_set) == 1 and len(clicks) != 1:
            return []
    for i, j in clicks:
        for d1 in range(-1, 2):
            for d2 in range(-1, 2):
                if board[i+d1][j+d2] == 0:
                    board[i+d1][j+d2] = 2
    count = [0, 0, 0]
    for i in range(2, R+2):
        for j in range(2, C+2):
            count[board[i][j]] += 1
    if count[0] != 0:
        return [] 
    return clicks
        
T = int(raw_input())
for case in range(1, T+1):
    R, C, M = [int(i) for i in raw_input().split()]
    print "Case #%d:" % case
    if C >= 4 and R*C-M > 2*C and (R*C-M-1) % C != 0:
        sys.stdout.write('c') 
        for i in range(1, R*C):
            if i % C == 0:
                sys.stdout.write('\n')
            c = '.' if i < R*C-M else '*'
            sys.stdout.write(c)
        sys.stdout.write('\n')
        continue 
    if R >= 4 and R*C-M > 2*R and (R*C-M-1) % R != 0:
        tmp = defaultdict(lambda: ['#']*C)
        for i in range(R):
            for j in range(C):
                if j < (R*C-M)/R:
                    tmp[i][j] = '.'
                elif j > (R*C-M)/R:
                    tmp[i][j] = '*'
                elif i < (R*C-M)%R:
                    tmp[i][j] = '.'
                else:
                    tmp[i][j] = '*'
        tmp[0][0] = 'c'
        for i in range(len(tmp)):
            print ''.join(tmp[i])
        continue
    orig = [0] * (R * C)
    for pos in itertools.combinations(range(R*C), M):
        board = orig[:]
        for _ in pos:
            board[_] = 1
        l = zip(*[iter(board)]*C)
        result = check(R, C, l)
        if len(result) != 0:
            ii, jj = result[0]
            ii, jj = ii-2, jj-2
            for i in range(R):
                for j in range(C):
                    if i == ii and j == jj:
                        sys.stdout.write('c')
                    elif l[i][j] == 1:
                        sys.stdout.write('*')
                    else:
                        sys.stdout.write('.')
                sys.stdout.write('\n')
            break
    else:
        print "Impossible"

#l = [[0],[0],[1]]
#print check(3, 1, l)



