import sys


def solveCase(case):
    D, N = map(int, sys.stdin.readline().split(" "))

    horses = [None] * N

    for horse in range(N):
        K, S = map(int, sys.stdin.readline().split(" "))
        horses[horse] = (K, S)

    horses.sort(key=lambda x:(-x[0], x[1]))

    time = 0

    for i in range(N):
        time = max(time, (D - horses[i][0]) / horses[i][1])

    speed = D / time
    print("Case #" + str(case) + ": " + str(speed))

T = int(sys.stdin.readline())

for t in range(T):
    solveCase(t + 1)

