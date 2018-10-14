l = 100
def solve(Q_):
    Q = [[],[]]
    for q in Q_:
        Q[q[0]].append(q[1])
    Q[0].append(0)
    Q[1].append(0)
    cur = [0,0]
    t = 0
    p = [0,0]
    for q in Q_:
        u = q[0]
        v = 1-u
        d = abs(cur[u]-q[1])+1
        t+=d
        cur[u] = q[1]
        p[u]+=1
        if Q[v][p[v]]>cur[v]:
            cur[v]+=min(Q[v][p[v]]-cur[v],d)
        else:
            cur[v]-=min(cur[v]-Q[v][p[v]],d)
    return t

fi = open("input.txt")
line = fi.readline()
T = int(line)
for test in range(T):
    line = fi.readline()
    a = line.split()
    n = int(a[0])
    quest = []
    for i in range(n):
        tmp = 0
        if a[i*2+1]=='O':
            tmp = 0
        else:
            tmp = 1
        quest.append((tmp,int(a[i*2+2])-1))
    print "Case #{0}: {1}".format(test+1,solve(quest))
fi.close()

