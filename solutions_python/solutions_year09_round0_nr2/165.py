import string

inf = 'B-large.in'
outf = 'out-l.txt'

def getrc(x):
    return [int(x), None]

def colorize(rows, h, w):
    ux = uy = 0
    si = ord('a')
    while uy < h:
        spread(rows, uy, ux, h, w, chr(si))
        si += 1
        #temp fix to test on random data
        if si > ord('z'): si = ord('a')
        (uy, ux) = next(uy, ux, h, w)
        while uy < h and rows[uy][ux][1]: 
            (uy, ux) = next(uy, ux, h, w)
        
def next(y, x, h, w):
    if x+1<w: 
        return (y, x+1)
    return (y+1,0)
        
def dir(rows, y, x, h, w):
    ca = rows[y][x][0]
    r='.'
    if y>0 and rows[y-1][x][0]<ca:
        r='n'
        ca = rows[y-1][x][0] 
    if x>0 and rows[y][x-1][0]<ca:
        r='w'
        ca = rows[y][x-1][0]
    if x<w-1 and rows[y][x+1][0]<ca:
        r='e'
        ca = rows[y][x+1][0] 
    if y<h-1 and rows[y+1][x][0]<ca:
        r='s'
        ca = rows[y+1][x][0] 
    return r 
    
def spread(rows, y, x, h, w, c):
    tv = [(y, x)]
    v = []
    
    while len(tv) > 0:
        point = tv.pop();
        y = point[0]; x = point[1]
        rows[y][x][1] = c
        al = rows[y][x][0]
        cdir = dir(rows, y, x, h, w)
        if y>0 and rows[y-1][x][1] is None and (cdir=='n' or dir(rows,y-1,x,h,w)=='s'):
            tv.append((y-1, x))
        if x<w-1 and rows[y][x+1][1] is None and (cdir=='e' or dir(rows,y,x+1,h,w)=='w'):
            tv.append((y, x+1))
        if y<h-1 and rows[y+1][x][1] is None and (cdir=='s' or dir(rows,y+1,x,h,w)=='n'):
            tv.append((y+1, x))
        if x>0 and rows[y][x-1][1] is None and (cdir=='w' or dir(rows,y,x-1,h,w)=='e'):
            tv.append((y, x-1))
            
    

def res(case, rows, out):
    if (case > 1): 
        out.write('\n')
    out.write("Case #" + str(case) + ":")
    for row in rows:
        out.write("\n")
        for i in range(len(row) - 1):
            out.write(row[i][1] + " ")
        out.write(row[len(row) - 1][1])

input = open(inf)
out = open(outf, 'w')
cases = int(input.readline())
#out system date
import time
print(str(time.time()))

for caseid in range(cases):
    dims = string.split(input.readline())
    h = int(dims[0])
    w = int(dims[1])
    rows = []
    for r in range(h):
        rows.append(map(getrc, string.split(input.readline())))
    colorize(rows, h, w)    
    res(caseid+1, rows, out)
    print(str(caseid) + " done")
print(str(time.time()))