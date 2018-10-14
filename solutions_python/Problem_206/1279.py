

t = int(input())

for i in range(1, t + 1):
    D, N = [int(s) for s in input().split(" ")]

    l = 0
    for j in range(N):
        K, S = [int(s) for s in input().split(" ")]

        t = (D - K) / S
        if t > l:
            l = t

    ns = D / l
    print("Case #{}: {}".format(i, ns))
