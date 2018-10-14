def solve(N, vines, D):
    d = [vines[i][0] for i in range(N)]
    l = [vines[i][1] for i in range(N)]
    p = {0: d[0]}
    k = 1
    for i in range(0, N):
        if i not in p:
#            print(p)
#            print(i)
            return "NO"
        if d[i] + p[i] >= D:
#            print(p)
            return "YES"
        for j in range(k, N):
            if d[j] > d[i] + p[i]:
                k = j
                break
            if j not in p:
                p[j] = min(d[j] - d[i], l[j])
            else:
                p[j] = max(p[j], min(d[j] - d[i], l[j]))
            k = j + 1
        else:
            k = N
#    print(p)
    return "NO"
            

T = int(input ())
for i in range(1, T + 1):
    N = int(input())
    vines = [tuple(map(int, input().split())) for j in range(N)]
    D = int(input())
    print("Case #%d: %s" % (i, solve(N, vines, D)))

