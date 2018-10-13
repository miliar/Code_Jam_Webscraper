from collections import Counter
for t in range(int(input())):
    (N,K) = [int(i) for i in input().strip().split(' ')]
    U = float(input())
    L = sorted([float(i) for i in input().strip().split(' ')])
    same = 1
    while U>0:
        for j in range(same,len(L)):
            if L[j]==L[j-1]: same+=1
            else: break
        diff = float('inf')
        if same!=len(L):
            diff = L[same]-L[0]
        if diff*same>U:
            diff = U/same
            for i in range(same):
                L[i]=L[i]+diff
            U = 0
        else:
            for i in range(same):
                L[i]=L[same]
            U-=(diff*same)
    a = 1
    #print(L)
    for b in L: a*=b
    #print(a)
    print("Case #{0}: {1}".format(t+1,round(a,6)))
        
    
    
