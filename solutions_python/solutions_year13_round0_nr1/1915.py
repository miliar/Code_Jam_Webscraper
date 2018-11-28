inf = open('foo.in', 'rU')
out = open('out.txt', 'w')
T = int(inf.readline())

def transpose(l) :
    out=[]
    for x in l[0] :
        out.append([])

    for i in range(len(l)) :
        for j in range(len(l[i])) :
            out[j].append(l[i][j])
    return out
    
def win(grid, sym) :
    match=([sym,sym,sym,sym], [sym, sym, sym, 'T'], ['T', sym, sym, sym])
    diagonal=[]
    diagonal2=[]
    for i in range(len(grid)) :
        diagonal.append(grid[i][i])
        diagonal2.append(grid[i][len(grid)-i-1])
    if sorted(diagonal) in match :
        return True
    if sorted(diagonal2) in match  :
        return True      
    for row in range(len(grid)) :
        if sorted(grid[row]) in match :
            return True
    t=transpose(grid)
    for col in range(len(t)) :
        if sorted(t[col]) in match :
            return True
            
def no_empty(grid) :
    t=0
    for x in grid :
        if '.' not in x :
            t=t+1
    if t==4 :
        return True
    return False
    

for case in range(1, T+1):
    board = []
    for x in range(4):
        board.append(list(inf.readline()[:-1]))
    if win(board, 'X'):
        out.write("Case #%d: X won\n" % case)
    elif win(board, 'O'):
        out.write("Case #%d: O won\n" % case)
    elif no_empty(board):
        out.write("Case #%d: Draw\n" % case)
    else:
        out.write("Case #%d: Game has not completed\n" % case)
    inf.readline()
    
    
