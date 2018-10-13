input = open('C-small-attempt0.in', 'r')
output = open('C-small-attempt0.out', 'w')
INF = 10**12
t = int(input.readline().rstrip())
for test in range(t):
    output.write("Case #" + str(test + 1) + ": ")
    n, q = map(int, input.readline().rstrip().split())
    horses = [list(map(int, input.readline().rstrip().split())) for i in range(n)]
    matr = [list(map(int, input.readline().rstrip().split())) for i in range(n)]
    routes = [list(map(int, input.readline().rstrip().split())) for i in range(q)]
    for nr in range(q):
        best = [INF] * n
        best[0] = 0
        for i in range(0, n-1):
            j = i
            s = matr[j][j + 1]
            while j < n - 1 and s <= horses[i][0]:
                j += 1
                best[j] = min(best[j], best[i] + s / horses[i][1])
                if j < n - 1:
                    s += matr[j][j + 1]
    print(best[n - 1], file = output)

input.close()
output.close()