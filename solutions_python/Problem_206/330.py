
T = int(input())
for case in range(T):
    vals = input().split()
    D,N = [int(v) for v in vals]
    
    horses = [[int(v) for v in input().split()] for _ in range(N)]
    
    #horses.sort(key=lambda x:-x[0])
    maxtime = -1
    for dis,speed in horses:
        disleft = D-dis
        time = disleft/speed
        #print(disleft,time)
        maxtime = max(maxtime,time)
    print("Case #%d: %.6f"%(case+1,D/maxtime))
        
    