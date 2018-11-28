tc = int(input())
for t in range(tc):
    N = list(map(int, input()))
    n = len(N)
    k = None
    for i in range(n - 1):
        if N[i] < N[i + 1]:
            k = i
        if N[i] > N[i + 1]:
            if k is None:
                if N[0] == 1:
                    r = '9' * (n - 1)
                else:
                    r = str(N[0] - 1) + '9' * (n - 1)
            else:
                r = ''.join(map(str, N[:k + 1] + [N[k + 1] - 1])) + '9' * (n - k - 2)
            break
    else:
        r = ''.join(map(str, N))
    print("Case #{}: {}".format(t + 1, r))
