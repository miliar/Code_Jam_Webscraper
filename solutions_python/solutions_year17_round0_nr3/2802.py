T= int(input())
for t in range(T):
    st = input().split()
    N, K = int(st[0]), int(st[1])
    used = [False for i in range(N+2)]
    used[0],used[-1] = True, True
    for k in range(K):
        positions = set()
        left_near = [0 for i in range(N+2)]
        right_near = [N+1 for i in range(N+2)]
        for p in range(1, N+1):
            if used[p-1]:
                left_near[p] = p-1
            else:
                left_near[p] = left_near[p-1]
        for p in reversed(range(1, N+1)):
            if used[p+1]:
                right_near[p] = p+1
            else:
                right_near[p] = right_near[p+1]
        # print(left_near)
        # print(right_near)
    
        for j in range(1, N+1):
            if not used[j]:
                L_s = j - left_near[j] - 1 
                R_s = right_near[j] - j  - 1 
                # print(L_s, R_s)
                positions.add((min(L_s, R_s),max(L_s, R_s), -j))
        cur_j = max(positions)
        used[-cur_j[2]]=True
        # print(used)
    print("Case #%s: %s %s"% (t+1, cur_j[1], cur_j[0]))


