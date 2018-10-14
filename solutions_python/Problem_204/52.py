def DFS(r,rowindex,store,ans,accept,use): # a kit using store[r]
    # starting from rowindex[r] + 1
    
    c = rowindex[r] + 1

    for i in range(c,P):
        a,b = store[r][i]
        a = max(a,accept[0])
        b = min(b,accept[1])
        if a <= b: # ok

            if r == N-1:
                return 1,use+[i]

            else:
                ans,use = DFS(r+1,rowindex,store,ans,(a,b),use+[i])
                return ans,use

    return 0,None
    


T = input()

for case in range(1,T+1):
    N,P = [int(_) for _ in raw_input().split()]

    R = [int(_) for _ in raw_input().split()]

    store = [[] for _ in range(N)]

    rowindex = [-1] * N # search no lefter than this index

    ans = 0
    
    for p in range(N):
        x = sorted([int(_) for _ in raw_input().split()])
        # t1 ... t2  x \in [0.9t,1,1t]
        # 0.9 t <= x
        # 1.1t >= x
        # t <= x/0.9
        # t >= x/1.1
        # [x/1.1 , x/0.9]

        for i in x:
            a,b = (i/1.1)/R[p],(i/0.9)/R[p]
            if a != int(a):
                a = int(a) + 1
            else:
                a = int(a)

            b = int(b)

            #a,b = a/R[_],
            store[p].append((a,b))
            
        #store.append(sorted([int(_) for _ in raw_input().split()]))


    ans = 0
    if N == 1:
        for i in range(P):
            if (store[0][i][0] <= store[0][i][1]) and (store[0][i][0] > 0 ) and (store[0][i][1] > 0):
                ans += 1

    else:    
        for i in range(P):
            if (store[0][i][0] <= store[0][i][1]) and (store[0][i][0] > 0 ) and (store[0][i][1] > 0):
                a,use = DFS(1,rowindex,store,ans,store[0][i],[i]) # a kit using store[0][i]
                if a == 1:
                    ans += a
                    rowindex = use
                    #print rowindex
                

    print "Case #%d: %d" % (case,ans)
