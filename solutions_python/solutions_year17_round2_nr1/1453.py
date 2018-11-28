tc_num = int(input())

def solve():
    D, N = map(int, input().split())
    horses = []
    for i in range(N):
        K, S = map(int, input().split())
        horses.append([K, S])

    horses.sort(key = lambda x: x[0], reverse=True)
    maxtime = 0
    for i, h in enumerate(horses):
        time = (D - h[0]) / h[1]

        if time > maxtime:
            maxtime = time
        h.append(time)

    print("{0:.6f}".format(D / maxtime))
    return



for i in range(tc_num):
    print("Case #{}: ".format(i + 1), end='')
    solve()
