T = int(input())
for n in range(T):
    K = input().split(' ')
    N, K = int(K[0]), int(K[1])
    mini, maxi = None, None
    if K == N:
        mini = 0
        maxi = 0
    elif K == 1:
        maxi = int(N / 2)
        mini = N - maxi - 1
    else:
        l = [N]
        count = [1]
        i = 0
        limit = N/2 + 1
        while i < K:
            max_value = max(l)
            if max_value == 1:
                mini = 0
                maxi = 0
                break
            s_n = count[l.index(max_value)]
            mini = int((max_value - 1) / 2)
            maxi = max_value -1 - mini
            if s_n >= K - i + 1:
                break
            elif s_n >= 1:
                l.remove(max_value)
                count.remove(s_n)
                if mini in l:
                    count[l.index(mini)] += s_n
                else:
                    l.append(mini)
                    count.append(s_n)
                if maxi in l:
                    count[l.index(maxi)] += s_n
                else:
                    l.append(maxi)
                    count.append(s_n)
                i += s_n
    print("Case #{}: {} {}".format(n+1, maxi, mini))
    
