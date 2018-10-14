n = int(input())

for i in range(n):
    C, F, X = list(map(float, input().split()))

    cookies = 0.
    r = 2.
    T = 0.
    while True:
        if X / r < C / r + X / (r+F):
            T += X / r
            break
        else:
            T += C / r
            r += F

    print("Case #{}: {}".format(i+1, T))
