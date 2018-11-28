T=int(input())
for t in range(T):
    line=input().split()
    D=int(line[0])
    N=int(line[1])
    besttime=0
    for i in range(N):
        line=input().split()
        K=int(line[0])
        S=int(line[1])
        left=D-K
        time= left/S
        besttime=max(besttime,time)
    bestspeed=D/besttime
    print("Case #" + str(t+1) + ": " + str(bestspeed))
