# Cruise contorl
# code jam - 
# uses python 3

T = int(input().strip())    # number of cases
for t in range(1,T+1):
    
    D, N = [int(c) for c in input().strip().split()]
    H = []
    for i in range(N):
        H.append([int(c) for c in input().strip().split()])
    	
    H.sort()

    TT = 0

    for i in range(N-1):
        x1,v1 = H[i]
        x2,v2 = H[i+1]

        t1 = (D-x1)/v1
        t2 = (D-x2)/v2 

        if (v1>v2) and ((t1*v2+x2)<D):
             TT += (x2-x1)/(v1-v2)
        else:
             TT = (D-x1)/v1

    x1,v1 = H[-1]
    t1 = (D-x1)/v1
    if TT<t1:
    	TT += (t1-TT)

    v1 = D/TT
                        
    print('Case #{}: {:.6f}'.format(t, v1))    