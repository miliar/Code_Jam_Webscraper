import sys, os, operator

def transform(arr,row,col,rows,cols):
    if row > rows -2 or col > cols -2:
        return False
    if arr[row][col] != '#' or arr[row+1][col] != '#' or arr[row][col+1] != '#' or arr[row+1][col+1 ] != '#':
        return False
    arr[row][col], arr[row+1][col], arr[row][col+1], arr[row+1][col+1] = '/','\\','\\','/'
    return arr

def transformAll(pic,rows,cols):
    for r in xrange(rows):
        for c in xrange(cols):
            if pic[r][c] == '#':
                if not transform(pic,r,c,rows,cols):
                    return False
    return pic


#f = open("sample-in.txt")
f = sys.stdin

cases = f.readline()
#print cases
#print int(cases)
for case in xrange(1,int(cases)+1):
    rows,cols = map(int,f.readline().split())
    pic = []
    for row in xrange(rows):
        pic.append(list(f.readline().rstrip()))
    #print pic
    print 'Case #%d:'%case
    pic = transformAll(pic,rows,cols)
    if not pic:
        print 'Impossible'
    else:
        for r in xrange(rows):
            print ''.join(pic[r])



