def check(board):
    x = board.count('X')
    o = board.count('O')
    t = board.count('T')
    dot = board.count('.')
    if x+t == 4:
        return 1
    elif o+t == 4:
        return 2
    elif dot != 0:
        return 3
    return 0

f = open('A-large.in','r')
g = open('A-large-output0','w')
n = int(f.readline())

for x in range(n):
    board=[]
    hv3ret = False
    ret = 0
    for i in range(4):
        board.append(f.readline())
        board[i] = board[i][:4]
    for i in range(4):
        ret = check(board[i])
        if ret == 1 or ret == 2:
            break
        if ret == 3:
            hv3ret = True
    if ret == 1:
        writ = 'Case #'+str(x+1)+': X won'
        g.write(writ)
        g.write('\n')
        if x<n-1:
            f.readline()
        continue
    elif ret == 2:
        writ = 'Case #'+str(x+1)+': O won'
        g.write(writ)
        g.write('\n')
        if x<n-1:
            f.readline()
        continue
        
    a=[[],[],[],[]]
    d=[[],[]]
    for i in range(4):
        a[i]=[board[p][i] for p in range(4)]
        print x,a[i],i,board[i][i],board[i][3-i]
        d[0].append(board[i][i])
        d[1].append(board[i][3-i])
        ret = check(a[i])
        if ret == 1 or ret == 2:
            break
        if ret == 3:
            hv3ret = True
    if ret == 1:
        writ = 'Case #'+str(x+1)+': X won'
        g.write(writ)
        g.write('\n')
        if x<n-1:
            f.readline()
        continue
    elif ret == 2:
        writ = 'Case #'+str(x+1)+': O won'
        g.write(writ)
        g.write('\n')
        if x<n-1:
            f.readline()
        continue

    for i in range(2):
        ret = check(d[i])
        if ret == 1 or ret == 2:
            break
        if ret == 3:
            hv3ret = True
        
    if ret == 1:
        writ = 'Case #'+str(x+1)+': X won'
        if x<n-1:
            f.readline()
        g.write(writ)
        g.write('\n')
        continue
    elif ret == 2:
        writ = 'Case #'+str(x+1)+': O won'
        g.write(writ)
        g.write('\n')
        if x<n-1:
            f.readline()
        continue
    elif hv3ret == True:
        writ = 'Case #'+str(x+1)+': Game has not completed'
        g.write(writ)
        g.write('\n')
        if x<n-1:
            f.readline()
        continue
    writ = 'Case #'+str(x+1)+': Draw'
    g.write(writ)
    g.write('\n')
    if x<n-1:
        f.readline()
f.close()
g.close()

