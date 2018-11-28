# 2^{S - K + 1} patterns to flip since flipping on the same spot will end up being the same.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    Dstr, Nstr = input().split()  # read a list of integers, 2 in this case
    D = int(Dstr)
    N = int(Nstr)
    Ks = []
    Ss = []
    for j in range(N):
        K, S = input().split()
        Ks.append(int(K))
        Ss.append(int(S))


    if N == 1:
        remain_dist = D - Ks[0] 
        remain_hours = float(remain_dist)/Ss[0]
        print("Case #{}: {}".format(i, D/remain_hours))
        continue

    remain_hours_max = 0.0
    for j in range(N):
        remain_dist = D - Ks[j] 
        remain_hours = float(remain_dist)/Ss[j]
        #print(remain_hours)
        remain_hours_max = max(remain_hours, remain_hours_max)
    
    print("Case #{}: {}".format(i, D/remain_hours_max))
                
