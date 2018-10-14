def lineWinner(l):
    oCnt = l.count('O')
    xCnt = l.count('X')
    tCnt = l.count('T')
    if (oCnt + tCnt == 4):
        return 0
    if (xCnt + tCnt == 4):
        return 1
    return -1

def winner(a):
    for i in range(0,4):
        t = lineWinner(a[i])
        if (t != -1):
            return t
        t = lineWinner([a[0][i],a[1][i],a[2][i],a[3][i]])
        if (t != -1):
            return t
    t = lineWinner([a[0][0],a[1][1],a[2][2],a[3][3]])
    if (t != -1):
        return t
    t = lineWinner([a[3][0],a[2][1],a[1][2],a[0][3]])
    if (t != -1):
        return t
    for i in range(0,4):
        if (a[i].count('.') > 0):
            return 2
    return -1

f = open('A-large.in','r')
g = open('A-large.out','w')
a = f.read()
b = a.split('\n')
d = ""

cases = (int)(b[0])

for i in range(0,cases):
    a = []
    for j in range(0,4):
        t = []
        for k in range(0,4):
            t.append(b[i*5+j+1][k])
        a.append(t)
    r = winner(a)
    if (r == 0):
        g.write("Case #"+(str)(i+1)+": O won\n")
    elif (r == 1):
        g.write("Case #"+(str)(i+1)+": X won\n")
    elif (r == 2):
        g.write("Case #"+(str)(i+1)+": Game has not completed\n")
    else:
        g.write("Case #"+(str)(i+1)+": Draw\n")

f.close()
g.close()
