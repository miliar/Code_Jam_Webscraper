from collections import defaultdict
#data = open('c.txt').read().split()
data = open('C-small-attempt1.in').read().split()
#data = open('c.test').read().split()
data.reverse()
DEAD = 3
T = int(data.pop())
    
for t in range(1, T+1):
    M, N = int(data.pop()), int(data.pop())
    
    # Oh god this is so inefficient but it's 3 AM and I just want to qualify =)
    def isboard(board, r, c, sz):
        chk = board[r][c]
        for i in range(sz):
            for j in range(sz):
                if board[r+i][c+j] == DEAD:
                    return False
                elif (board[r+i][c+j] + i + j) % 2 != chk:
                    return False
        return True
        
    def boardsize(board, r,c):
        if board[r][c] == DEAD:
            return 0
        biggest = 1
        for sz in range(2, min(M+1, N+1)):
            if isboard(board, r, c, sz):
                biggest = sz
            else:
                break
        return biggest
                
    def kill(board, r, c, sz):
        #print 'cutting out board of size', sz, 'from',r,c
        for i in range(r, r + sz):
            for j in range(c, c + sz):
                board[i][j] = DEAD
        
    def printb(board):
        for i in range(len(board)):
            print ''.join(map(str, board[i]))
    
    board = []
    for m in range(M):
        hx = data.pop()
        bn = bin(int(hx, 16))[2:]
        while len(bn) < N:
            bn = '0' + bn
        row = [1 if ch == '1' else 0 for ch in bn] + [DEAD]
        board.append(row)
    
    board.append([DEAD] * N)
    
    sizes = defaultdict(int)
    
    while True:
        bestsz = 0
        bestpos = (False, False)
        for r in reversed(xrange(M)):
            for c in reversed(xrange(N)):
                sz = boardsize(board, r, c)
                if sz >= bestsz:
                    bestpos = r,c
                    bestsz = sz
        #print bestsz, bestpos
        if bestsz > 1:
            kill(board, bestpos[0], bestpos[1], bestsz)
            sizes[bestsz] = sizes[bestsz] + 1
        else:
            if bestsz == 1:
                for i in range(M):
                    for j in range(N):
                        if board[i][j] != DEAD:
                            sizes[1] += 1
            break
    print "Case #{0}: {1}".format(t, len(sizes))
    for sz in reversed(sorted(sizes.keys())):
        print sz, sizes[sz]