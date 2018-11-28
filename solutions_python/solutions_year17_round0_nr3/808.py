def processGuys(N,K):
    spaces= {N:1}

    while K>0:
        largest= max(spaces.keys())
        if spaces[largest]>=K:
            return ((largest-1)//2, largest//2)

        allocated= spaces[largest]
        if (largest-1)//2 not in spaces:
            spaces[(largest-1)//2]=0
        if largest//2 not in spaces:
            spaces[largest//2]=0
        spaces[(largest-1)//2]+=allocated
        spaces[largest//2]+=allocated
        K-= allocated
        spaces.pop(largest)
T= int(input())

for case in range(T):
    N,K= [int(l) for l in input().split()]
    a1, a2= processGuys(N,K)
    print("Case #"+str(case+1)+":", a2, a1)
