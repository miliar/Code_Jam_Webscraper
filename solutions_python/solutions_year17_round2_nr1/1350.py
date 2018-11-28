T = int(input())
for t in range(T):
    D, N = list(map(int, input().split()))
    s = 0
    for n in range(N):
        x, y = list(map(int, input().split()))
        if (D-x)/y > s:
            s = (D-x)/y
    #print(s)
    res = D / s
    print("Case #{}: {}".format(t+1, res))
