'''
Created on 8 May 2010

@author: Jirasak.Chirathivat
'''

def move(board, dim):
    newboard = []
    for row in board:
        nRow = row.replace('.', '')
        nRow = '.' * (dim-len(nRow)) + nRow
        newboard.append(nRow)
    return newboard

def transpose(board, dim):
    tBoard = []
    for x in range(dim):
        new = ''
        for j in range(dim):
            new += board[j][x]
        tBoard.append(new)
    return tBoard

def checkRows(board, ch, k):
    check = ch * k
    for row in board:
        if row.find(check) >= 0:
            return True
    return False

def checkDiag2(board, ch, dim, k):
    check = ch * k
    for x in range(dim - k + 1):
        for y in range(dim - k + 1):
            yy = (dim-y) - 1
            tmp = board[x][yy]
            for z in range(1, k):
                tmp += board[x+z][yy - z]
            if tmp.find(check) >= 0:
                return True
    return False

def checkDiag(board, ch, dim, k):
    check = ch * k
    for x in range(dim - k + 1):
        for y in range(dim - k + 1):
            tmp = board[x][y]
            for z in range(1, k):
                tmp += board[x + z][y + z]
            if tmp.find(check) >= 0:
                return True
    return False

def solve(board, dim, k):
    moved = move(board, dim)
    movedX = transpose(moved, dim)
    r = False 
    b = False
    if checkRows(moved, 'R', k): 
        r = True
    elif checkRows(movedX, 'R', k):
        r = True
    elif checkDiag(movedX, 'R', dim, k): 
        r = True
    elif checkDiag2(movedX, 'R', dim, k): 
        r = True
    
    if checkRows(moved, 'B', k): 
        b = True
    elif checkRows(movedX, 'B', k):
        b = True
    elif checkDiag(movedX, 'B', dim, k): 
        b = True
    elif checkDiag2(movedX, 'B', dim, k): 
        b = True
    if r and b:
        return 'Both'
    if r:
        return 'Red'
    if b:
        return 'Blue'
    return 'Neither'

if __name__ == '__main__':
    readfile = file('a.in')
    lines = readfile.readlines()
    
    n = int(lines[0].strip())
    i = 1
    start = 1
    for jj in range(n):
        dim, k =  [int(x) for x in lines[start].strip().split(' ')]
        start += 1
        board = [x.strip() for x in lines[start:start+dim]]
        value = solve(board, dim, k)
        print 'Case #%s: %s' % (i, value)
        #print 'Case #%s:' % (i)
        start += dim
        i += 1 
    
    readfile.close()
