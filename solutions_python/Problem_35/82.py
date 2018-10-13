fin = open(input("input file: "))
fout = open(input("output file: "),"w")
from collections import deque
def iterxy(w,h):
    for y in range(h):
        for x in range(w):
            yield (x,y)
for testnum in range(1,int(fin.readline())+1):
    ch = [c for c in 'abcdefghijklmnopqrstuvwxyz']
    ch.reverse()
    h,w = tuple(int(s) for s in fin.readline().split())
    char = [[None]*h for i in range(w)]
    link = tuple(tuple([] for j in range(h)) for i in range(w))
    alt = [[0]*h for i in range(w)]
    for y in range(h):
        s = tuple(int(s) for s in fin.readline().split())
        for x in range(w):
            alt[x][y] = s[x]            
    for x,y in iterxy(w,h):
        a,l = 1000000,None
        if y>0 and alt[x][y]>alt[x][y-1]:
           a,l = alt[x][y-1],(x,y-1)
        if x>0 and alt[x][y]>alt[x-1][y] and alt[x-1][y] <a:
           a,l = alt[x-1][y],(x-1,y)
        if x<w-1 and alt[x][y]>alt[x+1][y] and alt[x+1][y] <a:
           a,l = alt[x+1][y],(x+1,y)
        if y<h-1 and alt[x][y]>alt[x][y+1] and alt[x][y+1] <a:
           a,l = alt[x][y+1],(x,y+1)
        if not l:continue
        link[x][y].append(l)
        link[l[0]][l[1]].append((x,y))
    for x,y in iterxy(w,h):
         if char[x][y] : continue
         char[x][y] = curchar = ch.pop()             
         q = deque()
         q.append((x,y))             
         while len(q)>0:
             x,y = q.popleft()
             for u,v in link[x][y]:
                 if char[u][v] : continue
                 char[u][v] = curchar
                 q.append((u,v))
    fout.write('Case #'+str(testnum)+':\n')
    for y in range(h):
        for x in range(w):
            fout.write(str(char[x][y]) + ' ')
        fout.write('\n')
fout.close()
fin.close()

    
