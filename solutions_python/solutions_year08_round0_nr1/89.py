def getinput(infile):
    s=int(infile.readline()[:-1])
    engines=[]
    for i in range(s):
        engines.append(infile.readline()[:-1])
    engines_dict=dict(zip(engines,range(s)))
    q=int(infile.readline()[:-1])
    query=[]
    for i in range(q):
        query.append(engines_dict[infile.readline()[:-1]])
    return (s,q,query)

def makegraph(s,q,querry):
    graph=[[False for x in querry] for y in querry]
    for i in range(q):
        used=[False for x in querry]
        n=0
        for j in range(i,q):
            if not used[querry[j]]:
                used[querry[j]]=True
                n+=1
                if n==s:
                    break
            graph[i][j]=True
    return graph

def bfs(q,graph):
    vis=[False for i in range(q+1)]
    vis[0]=True
    queue=[(0,0)]
    qs=0
    qe=1
    while qe>qs:
        x,t=queue[qs]
        #print x
        if x==q: return t
        qs+=1
        for i in range(q):
            if graph[x][i] and (not vis[i+1]):
               queue.append((i+1,t+1))
               qe+=1
               vis[i+1]=True

def main():
    infile=open("input.txt","r")
    outfile=open("output.txt","w")
    tests=int(infile.readline()[:-1])
    for i in range(tests):
        s,q,query=getinput(infile)
        graph=makegraph(s,q,query)
        #print i
        if q==0:
            outfile.write("Case #%d: %d\n" % (i+1,0))
        else:
            outfile.write("Case #%d: %d\n" % (i+1,bfs(q,graph)-1))
    outfile.close()
    infile.close()

if __name__ == "__main__":
    main()
