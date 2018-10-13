T = int(input())
for i in range(T):
    userIN = input().split(" ")
    N = int(userIN[0])
    K = int(userIN[1])
    #N = (N-K)//K
    #S1=N//2
    #S2=N-S1
    #if(i == T-1):
    #    print("Case #"+str(i+1)+": "+str(H)+" "+str(L),end="")
    #else:
    #    print("Case #"+str(i+1)+": "+str(H)+" "+str(L))
    while(K!=0):
        L = (N-1)//2
        H = N-1-L
        if(K%2==0):
            N = H
        else:
            N = L
        K = K//2
    #print("Case #"+str(i+1)+": "+str(H)+" "+str(L))
    if(i == T-1):
        print("Case #"+str(i+1)+": "+str(H)+" "+str(L),end="")
    else:
        print("Case #"+str(i+1)+": "+str(H)+" "+str(L))
