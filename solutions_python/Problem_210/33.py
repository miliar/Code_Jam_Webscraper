T = int(input())

for t in range(1, T+1):
    ac, aj = map(int, input().split())
    
    ac_list = sorted([(tuple(map(int, input().split())), 0) for _ in range(ac)])
    aj_list = sorted([(tuple(map(int, input().split())), 1) for _ in range(aj)])
    sum_c = sum(map(lambda x : x[0][1]-x[0][0], ac_list))
    sum_j = sum(map(lambda x : x[0][1]-x[0][0], aj_list))

    all_list = sorted(ac_list + aj_list)
    in_c, in_j, outer = [], [], []
    n = len(all_list)
    for i in range(n):
        if i < n-1:
            cur = all_list[i]
            nex = all_list[i+1]
            dif = nex[0][0]-cur[0][1]
        else:
            cur = all_list[n-1]
            nex = all_list[0]
            dif = nex[0][0]-cur[0][1]+1440
        if cur[1] != nex[1]:
            outer.append(dif)
        else:
            if cur[1] == 0:
                in_c.append(dif)
            else:
                in_j.append(dif)

    ans = len(outer)
    if sum(in_c) + sum_c > 720 or sum_j + sum(in_j) >  720:
        arr, ss = None, 0
        if sum(in_c) + sum_c > 720:
            arr = in_c
            ss = sum_c
        else:
            arr = in_j
            ss = sum_j

        arr.sort(reverse=True)
        val = sum(arr)
        for v in arr:
            ans += 2
            val -= v
            if val + ss <= 720:
                break

    print("Case #%d: %d" %(t, ans))
