T = int(input())

for t in range(1, T+1):
    D, N = [int(s) for s in input().split(" ")]
    max_time = 0
    k = 0
    s = 0
    
    for n in range(1, N+1):
        K, S = [int(s) for s in input().split(" ")]
        time = (D - K)/S

        if time > max_time:
            max_time = time
            k = K
            s = S

    distance = k
    speed = distance/max_time
    ans = speed + s

    print("Case #{}: {:.6f}".format(t, ans))
