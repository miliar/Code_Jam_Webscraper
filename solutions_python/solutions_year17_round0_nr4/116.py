import sys;

def tp(a,m,n):
    return [[a[i][j] for i in range(0,n)] for j in range(0,m)]

def stylePoints(g,n):
    p = 0;
    for i in range(0,n):
        for j in range(0,n):
            t = gg(g,n,i,j)
            if t != ".":
                p += 2 if t == "o" else 1;
    return p;

rows = []
cols = []
main = []
anti = []
def gg(g,n,x,y):
    return g[x*n+y]
def sg(g,n,x,y,t):
    g[x*n+y]=t
def isE(g,n,r,c):
    return gg(g,n,r,c) == '.'
def isO(g,n,r,c):
    return gg(g,n,r,c) == 'o'
def isXO(g,n,r,c):
    return gg(g,n,r,c) == 'x' or isO(g,n,r,c)
def isPlusO(g,n,r,c):
    return gg(g,n,r,c) == '+' or isO(g,n,r,c)
def populateRowColDiagData(g,n):
    global rows
    global cols
    global main
    global anti
    rows = [0 for i in range(0,n)]
    cols = [0 for i in range(0,n)]
    main = [0 for i in range(0,2*n-1)]
    anti = [0 for i in range(0,2*n-1)]

    for i in range(0,n):
        for j in range(0,n):
            if isXO(g,n,i,j):
                rows[i] += 1
                cols[j] += 1
            if isPlusO(g,n,i,j):
                main[j-i+n-1] += 1
                anti[i+j] += 1
def alterRCMAData(g,n,m):
    global rows
    global cols
    global main
    global anti

    i = m.p.x
    j = m.p.y
    if isXO(g,n,i,j) and m.o != 'x':
        rows[i] += 1
        cols[j] += 1
    if isPlusO(g,n,i,j) and m.o != '+':
        main[j-i+n-1] += 1
        anti[i+j] += 1
            
def getRowColNumber(g,n,i,j):
    dx = -1 if isXO(g,n,i,j) else 0;
    return max(rows[i] + dx, cols[j] + dx);
def getMainAntiNumber(g,n,i,j):
    dx = -1 if isPlusO(g,n,i,j) else 0;
    return max(main[j-i+n-1] + dx, anti[i+j] + dx);
    
class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y
class Model:
    def __init__(self, p, c, o):
        self.p = p
        self.c = c
        self.o = o
def checkPoint(g,n,x,y,lookingForO):
    rc = getRowColNumber(g,n,x,y)
    ma = getMainAntiNumber(g,n,x,y)

    if lookingForO:
        if not isO(g, n, x, y) and rc == 0 and ma == 0:
            found = True
            return {'found': True, 'model': Point(x, y)}
    else:
        if isE(g, n, x, y) and 0 <= rc <= 1 and ma == 0:
            found = True
            return {'found': True, 'model': Point(x, y)}
    return {'found':False}
def pyramid(g,n,lookingForO,bl):
    for i in range(0,(n+1)/2):
        for j in range(0,n-1-2*i):
            if not bl[i*n+i+j]:
                result = checkPoint(g, n, i, j + i, lookingForO);
                if result['found']:
                    return result
                else:
                    bl[i*n+i+j]=True
            if not bl[(i + j)*n+n - 1 - i]:
                result = checkPoint(g, n, i + j, n - 1 - i, lookingForO);
                if result['found']:
                    return result
                else:
                    bl[(i + j)*n+n - 1 - i]=True
            if not bl[(n - 1 - i)*n + n - 1 - i - j]:
                result = checkPoint(g, n, n - 1 - i, n - 1 - i - j, lookingForO);
                if result['found']:
                    return result
                else:
                    bl[(n - 1 - i)*n+n - 1 - i - j]=True
            if not bl[(n - 1 - i - j)*n+i]:
                result = checkPoint(g, n, n - 1 - i - j, i, lookingForO);
                if result['found']:
                    return result
                else:
                    bl[(n - 1 - i - j)*n+i]=True
    return {'found':False}
def plain(g,n,bl):
    for i in range(0,n):
        for j in range(0,n):
            if not bl[i*n+j]:
                rc = getRowColNumber(g,n,i,j)
                ma = getMainAntiNumber(g,n,i,j)
                if isE(g,n,i,j) and rc == 0 and 0 <= ma <= 1:
                    return {'found': True, 'model': Point(i, j)}
                else:
                    bl[i*n+j]=True
    return {'found':False}
def updateGrid(r,g,n,ms,t):
    if r['found']:
        p = r['model']
        m = Model(p, t, gg(g,n,p.x,p.y))
        sg(g,n,p.x,p.y,t)

        #ms = [ m for m in models if mvar.p.x!=m.p.x or mvar.p.y==m.p.y ]

        i = len(ms)-1
        while i>=0:
            mvar = ms[i]
            if (mvar.p.x==m.p.x and mvar.p.y==m.p.y):
                del ms[i]
            i-=1;
        ms.append(m)
        return m
    return None

def runOnce(g,n,ms,blo,blp,blx):
    
    m = updateGrid( pyramid(g, n, False,blp), g, n, ms, '+' )
    if m is None:
        m = updateGrid( pyramid(g, n, True,blo), g, n, ms, 'o' )
        
        if m is None:
            m = updateGrid( plain(g,n,blx), g, n, ms, 'x' )
    return m;

def solve(g,n,m):
    if n == 1:
        return "2 0" if g[0] == "o" else "2 1\no 1 1";
    populateRowColDiagData(g,n);

    badLuckO = [ False for i in range(0,n*n) ]
    badLuckPlus = [ False for i in range(0,n*n) ]
    badLuckX = [ False for i in range(0,n*n) ]

    models = []

    m = runOnce(g,n,models,badLuckO,badLuckPlus,badLuckX)
    rerun = not m is None
            
    while rerun:
        alterRCMAData(g,n,m);

        m = runOnce(g,n,models,badLuckO,badLuckPlus,badLuckX)
        rerun = not m is None

        #print "len(models)", len(models)

    return str(stylePoints(g, n)) + " " + str(len(models)) + "\n" + ("\n".join(map(lambda m: m.c + " " + str(m.p.x+1) + " " + str(m.p.y+1), models)));

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        n,m = map(int, f.readline().split())
        grid=["." for i in range(0,n*n)];
        #print "case:",i,n,m
        for i in range(0,m):
            x, r, c = f.readline().split(" ")
            r = int(r)
            c = int(c)
            sg(grid,n,r-1,c-1,x);
        
        file.write(str(solve(grid, n, m)) + "\n")
file.close()            








