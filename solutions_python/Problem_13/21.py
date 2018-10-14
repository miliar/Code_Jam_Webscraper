import sys

    

def run(gates, changable, nodes, M, V):
    v0=[None for x in range(M)]
    v1=[None for x in range(M)]
    v=[v0,v1]

    for i in range(len(nodes)):
        if nodes[i]==0:
            v0[(M-1)/2+i]=0
        else:
            v1[(M-1)/2+i]=0

    def logic(father, change):
        a=father*2+1
        b=a+1
        g=gates[father]

        if change: g=1-g

        res=[None, None]
        for va in [0,1]:
            if v[va][a]!=None:
                for vb in [0,1]:
                    r=None
                    if v[vb][b]!=None:
                        if g==0: # or
                            r=va or vb
                        else:
                            r=va and vb
                    
                    if r!=None:
                        c=v[va][a]+v[vb][b]+change
                        if res[r]==None or res[r]>c:
                            res[r]=c
        
        return res

    for i in range((M-1)/2-1, -1, -1):
        r=logic(i,0)            # no change

        if changable[i]==1:     # changalbe
            r1=logic(i,1)

            def combine(x,y):
                if min(x,y)==None:
                    if max(x,y)==None:
                        return None
                    else:
                        return max(x,y)
                else:
                    return min(x,y)

            r[0]=combine(r[0],r1[0])
            r[1]=combine(r[1],r1[1])

        v[0][i]=r[0]
        v[1][i]=r[1]

    res=v[V][0]
    if res==None: return "IMPOSSIBLE"
    return res

def go(name):
    f=file(name)

    line=f.readline().strip()
    total=int(line)
    for i in range(total):
        M,V=[int(x) for x in f.readline().strip().split()]
        gates=[]
        changable=[]
        for j in range((M-1)/2):
            G,C=[int(x) for x in f.readline().strip().split()]
            gates.append(G)
            changable.append(C)
        nodes=[]
        for j in range((M+1)/2):
            n=int(f.readline().strip())
            nodes.append(n)

        r=run(gates,changable, nodes, M, V)
        
        print "Case #%d:" %(i+1,),r
    d=f.read().split("\n")
    f.close()

try:
    fn=sys.argv[1]
except:
    print "Usage:\n", "python", sys.argv[0]+" input_file_name"
    sys.exit(1)

go(fn)
