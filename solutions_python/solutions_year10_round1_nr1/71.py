import sys

fin = open(sys.argv[1]+'.in', 'rU')
fout = open(sys.argv[1]+'.out', 'w')

T = int(fin.readline().strip())

def rotate(board):
    new = []
    for row in board:
        vals = filter(lambda x: x!='.', row)
        new.append(['.']*(len(row)-len(vals))+vals)
    return new

def find(board, r, c, direc, K):
    if K == 1:
        return board[r][c]
    else:
        newr, newc = r+direc[0], c+direc[1]
        if newr < 0 or newr >= len(board) or newc < 0 or newc >= len(board):
            return False # Off the board
        others = find(board, newr, newc, direc, K-1)
        if others == board[r][c] and others in ('R','B'):
            return board[r][c] # Same as before
        else:
            return False # Different

# Right, Down, Down-left, Down-right
directions = [(0,1),(1,0), (1,-1), (1,1)]

results = {(True,True): "Both",
           (True, False): "Red",
           (False, True): "Blue",
           (False, False): "Neither"}

for case in xrange(T):
    N,K = map(int, fin.readline().split())
    board = [list(fin.readline().strip()) for i in xrange(N)]
    board = rotate(board)
    wins = set()
    for r in xrange(N):
        for c in xrange(N):
            for d in directions:
                findings = find(board, r, c, d, K)
                if findings:
                    wins.add(findings)
    ans = ('R' in wins, 'B' in wins)
    fout.write("Case #%i: %s\n" % (case+1, results[ans]))

fin.close()
fout.close()