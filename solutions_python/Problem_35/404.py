f = open("B-large.in")

T = int(f.readline().strip())

def findsink(table, ind, flow):
    path = [ind]
    while 1:
        if flow[ind[0]][ind[1]]:
            return ["stop"] + path
        neighbors = []
        if ind[0] > 0:
            neighbors.append([table[ind[0]-1][ind[1]], 0, ind[0]-1, ind[1]])

        if ind[0] < len(table)-1:
            neighbors.append([table[ind[0]+1][ind[1]], 3, ind[0]+1, ind[1]])

        if ind[1] > 0:
            neighbors.append([table[ind[0]][ind[1]-1], 1, ind[0], ind[1]-1])

        if ind[1] < len(table[0])-1:
            neighbors.append([table[ind[0]][ind[1]+1], 2, ind[0], ind[1]+1])

        if neighbors:
            next = min(neighbors)
        else:
            return path

        if next[0] >= table[ind[0]][ind[1]]:
            return path

        ind = (next[2], next[3])
        path.append(ind)

fout = open("B-large.out", "w")

for case in range(1, T+1):
    H, W = map(int, f.readline().split())
    table = []
    flow = []
    for i in range(H):
        flow.append([None] * W)
        table.append(map(int, f.readline().split()))
            
    nextnum = 1
    sinks = {}

    for (i, row) in enumerate(table):
        for (j, tile) in enumerate(row):
            if flow[i][j]:
                continue

            indpath = findsink(table, (i, j), flow)
            if indpath[0] == "stop":
                for ind in indpath[1:]:
                    flow[ind[0]][ind[1]] = flow[indpath[-1][0]][indpath[-1][1]]
                
            elif indpath[-1] in sinks:
                for ind in indpath:
                    flow[ind[0]][ind[1]] = sinks[indpath[-1]]

            else:
                sinks[indpath[-1]] = nextnum
                for ind in indpath:
                    flow[ind[0]][ind[1]] = nextnum
                nextnum += 1

    nextlet = 'a'
    for row in flow:
        for n in row:
            if type(n) == int:
                for (ind, i) in enumerate(flow):
                    for(ii, j) in enumerate(i):
                        if j == n:
                            flow[ind][ii] = nextlet
            
                nextlet = chr(ord(nextlet)+1)
    
    fout.write("Case #%d:\n" % case)
    for row in flow:
        for (i, n) in enumerate(row):
            if i: fout.write(" ")
            fout.write(n)
        fout.write('\n')

fout.close()

    
