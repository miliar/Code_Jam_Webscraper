INF=10000000000000
EPS=1e-10
tcas=int(raw_input())
dirs={'v':(1,0),'<':(0,-1),'^':(-1,0),">":(0,1),".":(0,0)}
d2s=[[1,0],[0,1],[-1,0],[0,-1]]
def check(grid,start,d,r,c):
    at=start
    while(r>at[0]>=0 and c>at[1]>=0):
        cur=dirs[grid[at[0]][at[1]]]
        if(cur[0]+d[0]==0 and cur[1]+d[1]==0):
            return at
        elif(cur[0]!=0 or cur[1]!=0):
            return -2
        at[0]+=d[0]
        at[1]+=d[1]
    return -1

def put(ans,bads):
    if(ans!=-1 and ans!=-2):
        bads.append(ans)
for cas in xrange(1,tcas+1):
    r,c=map(int,raw_input().split())
    grid=[ raw_input() for i in xrange(r)]
    bads=[]
    for i in xrange(r):
        put(check(grid,[i,0],[0,1],r,c),bads)
        put(check(grid,[i,c-1],[0,-1],r,c),bads)
    for i in xrange(c):
        put(check(grid,[0,i],[1,0],r,c),bads)
        put(check(grid,[r-1,i],[-1,0],r,c),bads)
    ans='x'
    for i in bads:
        gdirs=0
        for d in d2s:
            if(check(grid,[i[0]+d[0],i[1]+d[1]],d,r,c)!=-1):
                gdirs+=1
        if(gdirs==0):
            ans="IMPOSSIBLE"
    if(ans=='x'):
        print "Case #{}: {}".format(cas,len(bads))
    else:
        print "Case #{}: {}".format(cas,ans)
