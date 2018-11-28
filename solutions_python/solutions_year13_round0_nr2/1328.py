import sys,functools

def test_board(N,M,board):
    row_maxes = [functools.reduce(max,board[i]) for i in range(0,N)]
    col_maxes = [functools.reduce(max,[board[j][i] for j in range(0,N)]) for i in range(0,M)]
    new_board = [list(map(lambda x: min(x,row_maxes[j]),col_maxes)) for j in range(0,N)]
    for x in range(0,N):
        for y in range(0,M):
            if(board[x][y] != new_board[x][y]): return "NO"
    return "YES"

f = open(sys.argv[1],'r')
n = int(next(f))
for i in range(0,n):
    N,M = map(int,next(f)[:-1].split(" "))
    board = [[] for x in [0]*N]
    for y in range(0,N): 
        board[y] = list(map(int, next(f)[:-1].split(" ")))
    print("Case #%d: %s"%(i+1,test_board(N,M,board)))

