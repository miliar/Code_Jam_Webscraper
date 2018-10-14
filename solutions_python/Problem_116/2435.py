import sys
import io

def rowwinner(board, row):
    initial = board[row][0]
    if initial == 'T':
        initial = board[row][1]
    if initial == '.':
        return None
    win = True
    for i in board[row][1:]:
        if i != initial and i != 'T':
            win = False
            break
    if win == True:
        return initial

def colwinner(board, col):
    win = True
    column = [c[col] for c in board[1:]]
    initial = board[0][col]
    if initial == 'T':
        initial = column[0]
    if initial == '.':
        return None
    for i in column:
        if i != initial and i != 'T':
            win = False
            break
    if win == True:
        return initial

def pdiagwinner(board):
    win = True
    diag = [board[i][i] for i in range(4)]
    initial = diag[0]
    #print("pdiag", initial, diag)
    if initial == 'T':
        initial = diag[1]
    if initial == '.':
        return None
    for i in diag:
        if i != initial and i != 'T':
            win = False
            break
    if win == True:
        return initial

def ndiagwinner(board):
    win = True
    diag = [board[3 - i][i] for i in range(4)]
    initial = diag[0]
    if initial == 'T' and i != 'T':
        initial = diag[1]
    if initial == '.':
        return None
    #print("ndiag", initial, diag)
    for i in diag:
        if i != initial and i != 'T':
            win = False
            break
    if win == True:
        return initial


f = io.open("A-large.in")
o = io.open("Output", "w")
testcases = int(f.readline()[:-1])
lines = [str(s.strip().upper()) for s in f.readlines()]
#print(lines)

for case in range(testcases):
    board = lines[4 * case + case : 4 * (case + 1) + case]
    #print(board)
    winner = None
    movesleft = False
    for i in range(4):
        if '.' in board[i]:
            movesleft = True
        r = rowwinner(board, i)
        if r:
            winner = r
            break
        c = colwinner(board, i)
        if c:
            winner = c
            break
    
    n = ndiagwinner(board)
    if n:
        winner = n
    p = pdiagwinner(board)
    if p:
        winner = p
    o.write(unicode("Case #" + str(case + 1) + ": "))
    if winner:
        o.write(unicode(winner + " won\n"))
    else:
        if movesleft:
            o.write(unicode("Game has not completed\n"))
        else:
            o.write(unicode("Draw\n"))

o.close()
