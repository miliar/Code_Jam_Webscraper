#Q4

def process_case():
    (H, W, R) = [int(i) for i in raw_input().split()]
    rocks= []
    
    for i in range(R):
        (r,c) = [int(i) for i in raw_input().split()]
        rocks.append((r-1, c-1))
        
    count = []
    for i in range(H):
        count.append([])
        for j in range(W):
            count[i].append(0)
    
    
    count[0][0]=1
    
    if (H,W)==(1,1) or (H,W)==(2,3) or (H,W) == (3,2):
        return 1
    elif H < 3 or W < 3:
        return 0
    
     

    count[1][2]=1
    
    if (1,2) in rocks:
        count[1][2] = 0

    count[2][1]=1
    
    if (2,1) in rocks:
        count[2][1] = 0
        
    if W > 4 and H > 2 and not (2, 4) in rocks:
        count[2][4] = 1
        
    if H > 4 and W > 2 and not (4,2) in rocks:
        count[4][2] = 1
    
    
    for i in range(3, H):
        for j in range(3, W):
            count[i][j]=(count[i-2][j-1] + count[i-1][j-2])%10007
            if (i,j) in rocks:
                count[i][j]=0
    
    
    
    return count[H-1][W-1]



numCases = int(raw_input())

for i in range(numCases):
            
    print "Case #"+str(i+1)+":", (process_case())