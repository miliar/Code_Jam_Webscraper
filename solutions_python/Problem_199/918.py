from collections import defaultdict
def bfs(s,k):
    n=len(s)
    q=[[s,0]]
    d=defaultdict(lambda:0)
    d[s]=1
    l=0
    while l!=len(q):
        x=q[l][0]
        #print x
        if x.count('+')==n:
            return q[l][1]
        for i in range(n-k+1):
            y=list(x)
            for j in range(i,i+k):
                if y[j]=='+':
                    y[j]='-'
                else:
                    y[j]='+'
            y=''.join(y)
            if d[y]==0:
                d[y]=1
                q.append([y,q[l][1]+1])
        l+=1
    return "IMPOSSIBLE"

t=int(raw_input())
for ii in range(t):
    s,k=raw_input().split()
    print "Case #"+str(ii+1)+": "+str(bfs(s,int(k)))
        
