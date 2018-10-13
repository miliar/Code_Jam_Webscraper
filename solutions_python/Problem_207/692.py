def solve(N, R, O, Y, G, B, V):
    half = N // 2
    if (R > half) or (Y > half) or (B > half):
        return "IMPOSSIBLE"

    res = []
    for i in range(N):
        res.append("")
    colors = [(R, "R"), (Y, "Y"), (B, "B")]
    colors.sort()

    if (colors[2][0] > (N // 3)):
        count = colors[2][0]
        i = 0
        while count > 0:
            res[i] = colors[2][1]
            i += 2
            count -= 1
        count = colors[1][0]
        if N % 2:
            i = N - 2
        else:
            i = N - 1
        while count > 0:
            res[i] = colors[1][1]
            i -= 2
            count -= 1
        count =  colors[0][0]
        i = 0
        while count > 0:
            if res[i] == "":
                res[i] = colors[0][1]
                count -= 1
            i += 1
    else:
        i = 0
        while N > 0:
            if R > 0:
                res[i] = "R"
                i += 1
                R -= 1
                N -= 1
            if Y > 0:
                res[i] = "Y"
                i += 1
                Y -= 1
                N -= 1
            if B > 0:
               res[i] = "B"
               i += 1
               B -= 1
               N -= 1

    return ''.join(res)

T = int(input())

for t in range(1, T+1):
    N, R, O, Y, G, B, V = [int(s) for s in input().split(" ")]

    res = solve(N, R, O, Y, G, B, V)
    print("Case #{}: {}".format(t, res))
