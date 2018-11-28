for t in range(int(input())):
    (c,j) = [int(i) for i in input().strip().split(' ')]
    L = []
    for i in range(c+j):
        x = [int(i) for i in input().strip().split(' ')]
        L.append(x)
    ex = 2
    L = sorted(L,key= lambda x: x[0])
    if c==2 or j==2:
        if 1440-L[1][1]+L[0][0]<720:
            if(L[1][0]-L[0][1]<720): ex = 4
    print("Case #{0}: {1}".format(t+1,ex))
    
        
