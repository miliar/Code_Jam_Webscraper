for I in range(int(input())):
    pancakes, K = input().split(" ")
    K = int(K)
    N = len(pancakes)

    totalflips = 0
    runningflips = 0
    rf = []

    for i in range(N-K+1):        
        if runningflips%2 == 0:
            if pancakes[i] == '+':
                rf.append(0)
            else:
                runningflips += 1
                totalflips += 1
                rf.append(1)
        else:
            if pancakes[i] != '+':
                rf.append(0)
            else:
                runningflips += 1
                totalflips += 1
                rf.append(1)
        if i >= K-1:
            runningflips -= rf[0]
            rf = rf[1:]
        
    
    solvable = True
    for i in range(N-K+1, N):
        
        if runningflips % 2 == 0:
            if pancakes[i] != '+':
                solvable = False
        else:
            if pancakes[i] == '+':
                solvable = False
        if i >= K-1:
            runningflips -= rf[0]
            rf = rf[1:]
        
        
    if solvable:
        print("Case #"+str(I+1)+": "+ str(totalflips))
    else:
        print("Case #"+str(I+1)+": "+ "IMPOSSIBLE")
    


