#infile = open("/Users/simple/Desktop/b.txt")
#infile = open('/Users/simple/Desktop/B-small-attempt0.in')
infile = open('/Users/simple/Desktop/B-large.in')

def traverse(start,m,H,W):
    visited = [start]
    nexts = [start]
    prev_min = m[start[0]][start[1]]
    while(True):
        nexts=[]
        #N,W,E,S 
        if start[0] - 1 >= 0:
            if 0 <= m[start[0]-1][start[1]] < prev_min:
                nexts.append( (start[0]-1, start[1]))
        if start[1] - 1 >= 0:
            if 0 <= m[start[0]][start[1]-1] < prev_min:
                nexts.append( (start[0], start[1]-1))
        if start[1] + 1 < W:
            if 0 <= m[start[0]][start[1]+1] < prev_min:
                nexts.append( (start[0], start[1]+1))
        if start[0] + 1 < H:
            if 0 <= m[start[0] +1][ start[1]] < prev_min:
                nexts.append( (start[0] +1 , start[1]))
        if len(nexts) == 0:
            return visited
        values = [ m[v[0]][v[1]] for v in nexts]
        min_v = min( values )
        start = nexts[values.index(min_v)]
        visited.append(start)
        prev_min = min_v

N = int( infile.readline().strip() )
for i in range(N):
    H, W = map( int, infile.readline().strip().split())
    m = []
    for h in range(H):
        m.append( list(map( int, infile.readline().strip().split())) )

    sinks = {}
    visited = set()
    while( len(visited) != H*W):
        max_v = -1
        for h in m:
            max_v = max(max(h), max_v)
            
        maxes = []
        for j, h in enumerate(m):
            for k, v in enumerate(h):
                if max_v == v:
                    maxes.append( (j,k))
        for t in maxes:
            result = traverse( t, m, H, W)
            m[t[0]][t[1]] = -1
            visited = visited | set(result)
            sinks.setdefault(result[-1], set())
            sinks[result[-1]] = sinks[result[-1]] | set(result)

    
    result = []
    for h in range(H):
        result.append([])
        for w in range(W):
            result[h].append(w)

#    print(repr(sinks))
    mins={}
    labels = {}
    for key in sinks.keys():
        mins[key] = min(sinks[key])
        labels[key] = mins[key]
        
    mins_label=dict(zip( sorted(mins.values()),[chr(97 + i) for i in range(len(mins))]))

    for key in labels.keys():
        labels[key] = mins_label[labels[key]]
        
    for j,key in enumerate(sorted(sinks.keys())):
#       print(key,sinks[key],j)
        for p in sinks[key]:
            result[p[0]][p[1]] = labels[key]

    print('Case #{}:'.format(i+1))
    for line in result:
        for c in line:
            print(c,end=' ')
        print()
