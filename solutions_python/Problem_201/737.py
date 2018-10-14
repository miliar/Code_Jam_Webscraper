import sys

name = "C-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = input().split()
    N = int(line[0])
    K = int(line[1])

    cnt = 1
    s = 0

    x = N
    xcnt = 0
    y = N
    ycnt = 1

    while s + cnt < K:
        s += cnt
        cnt *= 2

        nx1 = (x - 1) // 2
        nx2 = x // 2

        ny1 = (y - 1) // 2
        ny2 = y // 2

        x = nx1
        y = ny2
		
        nxcnt = 0
        nycnt = 0

        if nx1 == x:
            nxcnt += xcnt
        elif nx1 == y:
            nycnt += xcnt

        if nx2 == x:
            nxcnt += xcnt
        elif nx2 == y:
            nycnt += xcnt

        if ny1 == x:
            nxcnt += ycnt
        elif ny1 == y:
            nycnt += ycnt

        if ny2 == x:
            nxcnt += ycnt
        elif ny2 == y:
            nycnt += ycnt

        xcnt = nxcnt
        ycnt = nycnt
               
    res = y if K-s <= ycnt else x

    print("Case #" + str(testCase) + ": " + str(res // 2) + " " + str((res - 1) // 2))
