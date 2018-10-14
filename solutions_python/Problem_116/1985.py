LEN = 4
def test(i,j,T):
    if i > 3 or (i==3 and T):
        return j + " won"
    return False

def rowSrch(players, board): 
    for i in board:
        for j in players:
            a = test(i.count(j),j,'T' in i)
            if a: return a
    return False

def colSrch(players, board):
    for i in players:
        for j in range(LEN):
            T = False
            cnt = 0
            for row in board:
                if row[j] == i:
                    cnt+=1
                if row[j] == 'T':
                    T = True
            a = test(cnt,i,T)
            if a: return a
    return False

def diagSrch(players,board):
    for j in players:
        cnt = 0
        T = False
        for i in range(LEN):
            if board[i][i] == j:
                cnt += 1
            if board[i][i] == 'T':
                T = True
        a = test(cnt, j, T)
        if a: return a
        cnt = 0
        T = False
        for i in range(LEN-1,-1,-1):
            if board[LEN-1-i][i] == j:
                cnt += 1
            if board[LEN-1-i][i] == 'T':
                T = True
        a = test(cnt, j, T)
        if a: return a
    return False

def tic2(fname):
    with open(fname) as f:
        lines = filter(bool, f.read().splitlines())
    n = int(lines.pop(0))
    q = 1; 
    players = ['X', 'O']
    # clear file
    with open('tictactoe6.out', 'w') as f:
        f.write('')
    while lines:
        board = []
        sol = 'Draw'
        for i in range(4):
            board.append(lines.pop(0))
        for z in board:
            print z
        r = rowSrch(players,board)
        if not r:
            c = colSrch(players, board)
            if not c:
                d = diagSrch(players,board)
                if not d:
                    for z in board:
                        print z.find('.')
                        if z.find('.') >= 0:
                            sol = "Game has not completed"
                            break
                else: sol = d  
            else: sol = c
        else:     sol = r
        
        with open('tictactoe6.out', 'a') as f:
            print q, sol,"\n\n"
            f.write("Case #%d: %s\n" % (q, sol))
        q += 1
tic2("A-large.in")
