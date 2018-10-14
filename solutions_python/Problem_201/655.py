import math

def bath(N,K):
    #print (N, " ",K)
    if N == 1:
        if K > 1:
            print("ERROR")
            return 0
        return (0,0)
    if K == 1:
        mid = math.ceil(N/2)     
        return (mid-1,N-mid)
    mid = math.ceil(N/2)
    Ls = mid-1
    Rs = N-mid
    k = math.ceil(K/2)
    p1 = k-1
    p2 = K-k
    if Ls == Rs:
        return bath(Ls,max(p1,p2))
    elif p1 == p2:
        return bath(min(Ls,Rs),p1)
    else:
        return bath(max(Ls,Rs),max(p1,p2))
    
num = int(input())
    
i = 1
while i <= num:
    
    line = input()
    lst = line.split(" ")
    N = int(lst[0])
    K = int(lst[1])
    ans = bath(N,K)
    #print(ans)
    
    s = 'Case #' + str(i) + ': ' + str(max(ans)) + ' ' + str(min(ans))
    print(s)
        
    i += 1    