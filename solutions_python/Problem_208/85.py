T=int(input())
for t in range(T):
    N=int(input().split()[0])
    horses=[]
    for i in range(N):
        line=input().split()
        horses.append([int(line[0]),int(line[1])])
    dists=[]
    for i in range(N):
        line=input().split()
        if i<N-1:
            dists.append(int(line[i+1]))
            if int(line[i+1])==-1:
                print ("FEL")
    Q1=input().split()
    times=[-1 for i in range(N)]
    times[0]=0
    for i in range(1,N):
        best=999999999999999
        for j in range(i):
            horses[j][0]-=dists[i-1]
            if horses[j][0]>=0:
                times[j]+= dists[i-1]/horses[j][1]

                best=min(best,times[j])
        times[i]=best
    print("Case #" + str(t+1) + ": " + str(times[-1]))
        
