

def solve(nodes,inner,root,wanted):
    if nodes[root][0]==wanted:
        return 0
    if root >= inner:
        return 100000 #impossible
    
    canchange = (nodes[root][2]==1)
    if nodes[root][1]==1: #and
        if wanted==1:
            left=solve(nodes,inner,root*2+1,1)
            right=solve(nodes,inner,root*2+2,1)
            if canchange:
                return min(left+right,1+min(left,right))
            else:
                return left+right
        if wanted==0:
            left=solve(nodes,inner,root*2+1,0)
            right=solve(nodes,inner,root*2+2,0)
            return min(left,right)

    if nodes[root][1]==0: #or
        if wanted==0:
            left=solve(nodes,inner,root*2+1,0)
            right=solve(nodes,inner,root*2+2,0)
            if canchange:
                return min(left+right,1+min(left,right))
            else:
                return left+right
        if wanted==1:
            left=solve(nodes,inner,root*2+1,1)
            right=solve(nodes,inner,root*2+2,1)
            return min(left,right)




f = open(r'C:\goog\A-large.in')

numcases=int(f.readline())
for case in range(numcases):
    line=f.readline().strip()

    (M,V) = map(int, line.split(' '))
    inner = (M-1)//2
    leaf  = (M+1)//2
    
    nodes=[]
    
    for i in range(M):
        line=f.readline().strip()
        if i < inner:
            (G,C)=map(int, line.split(' '))
            nodes.append([-1,G,C])
        else:
            I=int(line)
            nodes.append([I,-1,-1])
            
    innerrange=range(inner)
    innerrange.reverse()
    for i in innerrange:
        if nodes[i][1]==1:
            #and
            nodes[i][0]=nodes[2*i+1][0]*nodes[2*i+2][0]
        else:
            #or
            nodes[i][0]=max(nodes[2*i+1][0], nodes[2*i+2][0])

    sol=solve(nodes,inner,0,V)
    if sol>10000:
        solu="IMPOSSIBLE"
    else:
        solu=str(sol)

    print "Case #" + str(case+1) + ": " + solu
            

        






