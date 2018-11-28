import sys,re
import string
def valid(y,x):
    if y>=0 and y<H and x>=0 and x<W: return True
    return False

def flowto(y,x):
    ff = '.'
    g=grid[y][x]
    if y!=H-1:
        if grid[y+1][x] < g:
            ff=(y+1,x)
            g=grid[y+1][x]+1
    if x!=W-1:
        if grid[y][x+1] < g:
            ff=(y,x+1)
            g=grid[y][x+1]+1
    if x!=0:
        if grid[y][x-1] < g:
            ff=(y,x-1)
            g=grid[y][x-1]+1
    if y!=0:
        if grid[y-1][x] < g:
            ff=(y-1,x)
            g=grid[y-1][x]+1
    #print "fti##",
    #print (y,x),
    #print ff
    return ff


f=open( sys.argv[1])
N=int(f.readline().strip())
for n in xrange(N):
    (H , W) = f.readline().strip().split()
    H=int(H)
    W=int(W)
    grid=[]
    res=[]
    nsink=0
    for i in range(H):
        grid.append([int(x) for x in f.readline().strip().split()])
        res.append(["."]*W)
    for yy in range(H):
        for xx in range(W):
            if res[yy][xx] != '.':
                continue
            res[yy][xx]=chr(ord('a')+nsink)
            nsink+=1
            basin= res[yy][xx]
            #print basin
            q=[]
            q.append((yy,xx,yy+1,xx))
            q.append((yy,xx,yy-1,xx))
            q.append((yy,xx,yy,xx+1))
            q.append((yy,xx,yy,xx-1))
            while len(q):
                (y,x,y1,x1) = q.pop(0)
                if not valid(y1,x1): continue
                if res[y1][x1]!='.': continue    
                #print y,x,y1,x1
                if flowto(y1,x1) == (y,x) or flowto(y,x)==(y1,x1):
                    #print "MM"+str((y1,x1))
                    res[y1][x1]=basin
                    q.append((y1,x1,y1+1,x1))
                    q.append((y1,x1,y1-1,x1))
                    q.append((y1,x1,y1,x1+1))
                    q.append((y1,x1,y1,x1-1))
    print "Case #"+str(n+1)+":"
    for r in res:
        print " ".join(list(r))

