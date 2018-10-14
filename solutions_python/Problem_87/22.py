

def run():
    f=open("input.in")
    g=open("out.txt",'w')
    num = int(f.readline())
    for i in range(num):
        g.write("Case #%d: " % (i+1))
        [X,S,R,runtime,N]=map(int,f.readline().split())
        walkways = []
        nopath = 0
        cur = 0
        for j in range(N):
            [B,E,W]=map(int,f.readline().split())
            nopath=B-cur+nopath
            cur = E
            walkways.append((W,E-B))
        nopath = nopath + X-cur
        walkways.append((0,nopath))
        walkways.sort()
        unused = float(runtime)
        T = 0.0
        for path in walkways:
            if unused>0:
                delta = 1.0*path[1]/(path[0]+R)
                if delta<unused:
                    T=T+delta
                    unused = unused-delta
                else:
                    left = 1.0*(path[1]-(path[0]+R)*unused)
                    T=T+unused+1.0*left/(path[0]+S)
                    unused = -1
            else:
                T=T+1.0*path[1]/(path[0]+S)
        g.write("%.9f\n" %(T))                   
    f.close()
    g.close()
    
