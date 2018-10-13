
t = int(input())
for tc in range(1,t+1):
    d,n = [int(x) for x in input().split()]
    k = [0]*n
    s = [0]*n
    for i in range(n):
        k[i], s[i] = [int(x) for x in input().split()]

    dist = [d-k[i] for i in range(n)]
    time = [dist[i]/s[i] for i in range(n)]
    t_s = max(time)
    k_me = d/t_s
    print('Case #{}: {}'.format(tc, k_me))
