
import sys

file1 = open('B-small-attempt1.in','r')
file2 = open('B-small-attempt1.out','w')
sys.stdin = file1
sys.stdout = file2

#next = [[0,-1],[-1,0],[0,1],[1,0]]
next = [[-1,0],[0,-1],[0,1],[1,0]]
words = ['a','b','c','d','e','f','g','h','i','g','k','l',
         'm','n','o','p','q','r','s','t','u','v','w','x',
         'y','z']
index = 0

def check(x,y,h,w):
    if (x >= 0 and x < h and y >= 0 and y < w):
        return True
    return False

def change(maps2,ch,h,w):
    for i in xrange(h):
        for j in xrange(w):
            if maps2[i][j] == '.':
                maps2[i][j] = ch

def dfs(maps,maps2,x,y,h,w):

    if maps2[x][y] == '#':
        maps2[x][y] = '.'
    else:
        change(maps2, maps2[x][y], h, w)
        return True
        
    minx = -1
    miny = -1
    minvalue = maps[x][y]
    for i in xrange(4):
        dx = x+next[i][0]
        dy = y+next[i][1]
        if check(dx,dy,h,w):
#            print dx,dy,maps,h,w
            if maps[dx][dy] < minvalue:
                minx = dx
                miny = dy
                minvalue = maps[dx][dy]
    if minx != -1:
        return dfs(maps, maps2, minx, miny, h, w)
    return False
        
t = int(sys.stdin.readline())

for caseId in xrange(t):
    index=0
    line = sys.stdin.readline().strip()
    s = line.split()
    h = int(s[0])
    w = int(s[1])
    
    maps = []
    maps2 = []
    for i in xrange(h):
        maps2.append(['#'] * w)
    for i in xrange(h):
        line = sys.stdin.readline().strip()
        s = line.split()
        temp = map(int,s)
        maps.append(temp)
    
    for i in xrange(h):
        for j in xrange(w):
            if maps2[i][j] == '#':
                if dfs(maps, maps2, i, j, h, w)  == False:
                    change(maps2, words[index], h, w)
                    index += 1
        
    print "Case #%d:" % (caseId+1)
    for i in xrange(h):
        for j in xrange(w):
            print  maps2[i][j],
        print




file1.close()
file2.close()

