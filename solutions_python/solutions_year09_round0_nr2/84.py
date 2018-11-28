'''
Created on 3 Sep 2009

@author: Maksims Rebrovs
'''
data = open("b.in")
T = int(data.readline())
allmaps = []
for i in range(T):
    H,W = map(int, data.readline().split(" "))
    currentmap = []
    for j in range(H):
        row = map(int, data.readline().split(" "))
        currentmap.append(row)
    allmaps.append(currentmap)
maxmark = 0
def flowTo(m, x,y, maxX, maxY):

    candidates = filter(lambda a : a[0] >= 0 and a[0] < maxX and a[1] >=0 and a[1] < maxY and m[y][x] > m[a[1]][a[0]], [(x,y-1), (x-1, y), (x+1,y), (x, y+1)])
    if len(candidates) == 0: return (x,y)
    #print candidates
    minp = candidates[0]
    #print minp
    minh = m[minp[1]][minp[0]]
    for p in candidates:
        #print p
        if m[p[1]][p[0]] < minh:
            minh = m[p[1]][p[0]]
            minp = p
    return minp

def makeGraph(m):
    graph = [[() for i in range(len(m[j]))] for j in range(len(m))]
    for y in range(len(m)):
        for x in range(len(m[y])):
            #print x, y
            graph[y][x] = flowTo(m, x, y, len(m[y]), len(m))
    #print graph
    return graph

def inverseGraph(g):
    result = [[[] for i in range(len(g[j]))] for j in range(len(g))]
    for y in range(len(g)):
        for x in range(len(g[y])):
            result[g[y][x][1]][g[y][x][0]].append((x,y))
    #print result
    return result

def markAll(m):
    G = inverseGraph(makeGraph(m))
    unmarked = []
    marks = [[0 for i in range(len(m[j]))] for j in range(len(m))]
    for y in range(len(m)):
        for x in range(len(m[y])):
            unmarked.append((m[y][x], x, y))
    unmarked.sort()
    umc = map(lambda x : (x[1], x[2]), unmarked)
    currentmark = 1
    while (len(umc) > 0):
        vr = umc[0]
        #print vr
        umc.remove(vr)
        #print umc
        x, y = vr
        marks[y][x] = currentmark
        prevfront = [(x,y)]
        while True:
            front = []
            for p in prevfront:
                x,y = p
                front+=filter(lambda p : (p in umc), G[y][x])
            
            if len(front) == 0: break
            
            for p in front:
                x,y = p
                marks[y][x] = currentmark
                #print x,y
                umc.remove((x,y))
            
            prevfront = front
        currentmark+=1
    return marks

for nummap in range(T):

    marks =  markAll(allmaps[nummap])
    transt = ['*' for i in range(101)]
    cl = 'a' 
    for y in range(len(marks)):
        for x in range(len(marks[y])):
            #print marks[y][x]
            if transt[marks[y][x]] == '*':
                transt[marks[y][x]] = cl
                cl = chr(ord(cl) + 1)
    print "Case #" + str(nummap+1) + ":"
    for line in marks:
        print  reduce(lambda x, y: x+' ' +y, map(lambda x : transt[x],line))
            
                