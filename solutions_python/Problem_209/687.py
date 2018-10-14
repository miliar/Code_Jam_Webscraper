from math import pi
with open("input.txt","r") as reader, open("output.txt","w") as writer:
    cases = int(reader.readline())
    for cs in range(cases):
        n,k = map(int,reader.readline().split())
        cakes = []
        for _ in range(n):
            cakes.append(tuple(map(int,reader.readline().split())))
        cakes = sorted(cakes,reverse=True)
        dp = [[0 for _ in range(n)] for _ in range(k+1)]
        for j in range(n):
            dp[1][j] = (cakes[j][0] ** 2 + 2 * cakes[j][0] * cakes[j][1]) * pi
        for i in range(2,k+1):
            for j in range(n):
                for h in range(j):
                    if cakes[h][0] >= cakes[j][0]:
                        dp[i][j] = max(dp[i][j],dp[i-1][h]+ 2 * cakes[j][0] * cakes[j][1] * pi)
        answer = 0
        for j in range(n):
            answer = max(dp[k][j],answer)
        writer.write("Case #{}: {}\n".format(cs+1,answer))
