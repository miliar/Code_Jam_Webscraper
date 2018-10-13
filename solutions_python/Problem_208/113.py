fin = open("C-small-attempt0.in","rt")
fout = open("OUTPUT.txt","wt")

t = fin.readline().rstrip('\n')
t = int(t)

#a = set([0,5])
#b = set([0,2])
#print a.union(b)

def getD(travel,e,s,n,d):
    cityset = set()
    for x in travel[n]:
        if x[0]<0: continue
        if e<x[0]: break
        cityset = cityset.union(getD(travel,e-x[0],s,x[1],d+x[0]))
    cityset.add((n,float(d)/float(s)))
    return cityset

def dij(start,dest,g):
    vis = set()
    q = [(0.0,start)]
    while len(q) > 0:
        cur = q.pop(0)
        if cur[1] == dest: return cur[0]
        if cur[1] in vis: continue
        vis.add(cur[1])
        for x in g[cur[1]]:
            q.append((g[cur[1]][x]+cur[0],x))
        q.sort()

for case in range(1,t+1):
    n = fin.readline().rstrip('\n')
    n = n.split(" ")
    q = int(n[1])
    n = int(n[0])

    towns = [0 for x in range(n)]
    
    for town in range(n):
        e = fin.readline().rstrip('\n')
        e = e.split(" ")
        s = int(e[1])
        e = int(e[0])
        towns[town] = (e,s)

    travel = []
    for town in range(n):
        others = fin.readline().rstrip('\n')
        others = others.split(' ')
        others = [int(x) for x in others]
        for x in range(n):
            others[x] = (others[x],x)
        others.sort()
        travel.append(others)

    rmap = {}
    for x in range(n):
        rmap[x] = {}
        tmap = getD(travel,towns[x][0],towns[x][1],x,0)
        for y in tmap:
            if y[0] == x: continue
            if y[0] in rmap[x]: rmap[x][y[0]] = min(rmap[x][y[0]],y[1])
            else: rmap[x][y[0]] = y[1]
    print rmap
    dists = []
    for k in range(q):
        others = fin.readline().rstrip('\n')
        others = others.split(' ')
        others = [int(x) for x in others]
        dists.append(str(dij(others[0]-1,others[1]-1,rmap)))
    dists = " ".join(dists)

        
    sout = "Case #"+str(case)+": "
    sout += dists
    print sout
    fout.write(sout+'\n')

fout.close()














