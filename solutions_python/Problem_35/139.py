import sys

inp = open(sys.argv[1])

T = int(inp.readline())

def union(graph,p,q):
    if graph[p] != graph[q]:
        t = graph[q]
        for i in range(0, len(graph)):
            if graph[i] == t:
                graph[i] = graph[p]

def connect(x,y,status,graph,W,H):
    if status == 'SINK': return
    p = (W*y) + x
    if status == 'NORTH':
        q = (W*(y-1)) + x
    elif status == 'WEST':
        q = (W*y) + (x-1)
    elif status == 'EAST':
        q = (W*y) + (x+1)
    else:
        q = (W*(y+1)) + x

    union(graph,p,q)    
    
for t in range(0,T):
    line = inp.readline()

    H = int(line.split(' ')[0])
    W = int(line.split(' ')[1])

    graph = [x for x in range(0,(H*W))]

    shed = []
    
    for i in range(0,H):
        shed += [map(int,inp.readline().split(' '))]

    for y in range(0,H):
        for x in range(0,W):
            status = 'SINK'
            alt = shed[y][x]
            if y > 0 and alt > shed[y-1][x]:
                status = 'NORTH'
                alt = shed[y-1][x]
            if x > 0  and alt > shed[y][x-1]:
                status = 'WEST'
                alt = shed[y][x-1]
            if x < W-1 and alt > shed[y][x+1]:
                status = 'EAST'
                alt = shed[y][x+1]
            if y < H-1 and alt > shed[y+1][x]:
                status = 'SOUTH'
                alt > shed[y+1][x]

            connect(x,y,status,graph,W,H)

    label_ord = 97
    for i in graph:
        if type(i) == int:
            for j in range(0,len(graph)):
                if graph[j] == i:
                    graph[j] = chr(label_ord)
            label_ord += 1

    print "Case #%d:" % (t+1)
    for i in range(0,H):
        print ' '.join(graph[i*W:i*W+W])
        


    
    
            
    
inp.close()
