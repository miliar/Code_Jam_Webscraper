def solve():
    N, V, X = input().split()
    N = int(N)
    V = float(V)
    X = float(X)
    speeds = []
    temps = []
    for i in range(N):
        v, x = map(float, input().split())
        speeds.append(v)
        temps.append(x)
    if max(temps) < X or min(temps) > X:
        return "IMPOSSIBLE"
    if len(temps) == 1:
        if temps[0] == X:
            return "{0:.7f}".format(V / speeds[0])
        else:
            return "IMPOSSIBLE"
    if temps[1] == temps[0]:
        if temps[0] == X:
            return "{0:.7f}".format(V / (speeds[0] + speeds[1]))
        else:
            return "IMPOSSIBLE"
    V1 = V * ((X - temps[0]) / (temps[1] - temps[0]))
    T1 = V1 / speeds[1]
    V0 = V - V1
    T0 = V0 / speeds[0]
    return "{0:.7f}".format(max([T0, T1]))


tcnum = int(input())

for tc in range(1, tcnum+1):
    print("Case #{}: {}".format(tc, solve()))