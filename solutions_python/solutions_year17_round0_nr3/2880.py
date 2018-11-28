t = int(input())

for c in range(1,(t+1)):
    N , K = [int(s) for s in input().split(" ")]

    FO = -1
    LO = N
    m = 0
    M = 0

    A = [-1,N]

    #for i in range(0,N):
        #A.append('.')

    for i in range(1,K+1):
        x = int((FO+LO)/2)
        #print("x = ",x)

        A.append(x)
        A.sort()

        if(i == K):
            LS = x - FO
            RS = LO - x
            m = min(LS,RS)-1
            M = max(LS,RS)-1
        else:
            maxD = 0
            for j in range(0,len(A)-1):

                if(A[j+1]-A[j]>maxD):
                    maxD = A[j+1]-A[j]
        
                    FO = A[j]
                    LO = A[j+1]
                  
                   
    print("Case #{}: {} {}".format(c,M,m))
    

                    
                
            

            
