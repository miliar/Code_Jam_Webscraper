import sys

t = int(sys.stdin.readline())

for i in range(t):
    m, n = map(int, sys.stdin.readline().split())
    arr = []
    arrl = [[True for x in range(n)] for y in range(m)]
    arru = [[True for x in range(n)] for y in range(m)]
    arrd = [[True for x in range(n)] for y in range(m)]
    arrr = [[True for x in range(n)] for y in range(m)]

    for j in range(m):
        line = map(int, sys.stdin.readline().split())
        arr.append(line)

    for y in range(m):
        for x in range(n):
            if x > 0:
                if arr[y][x] > arr[y][x-1]:
                    arrl[y][x] = True
                elif arr[y][x] == arr[y][x-1]:
                    arrl[y][x] = arrl[y][x-1]
                else:
                    arrl[y][x] = False

            if x < n-1:
                if arr[y][x] > arr[y][x+1]:
                    arrr[y][x] = True
                elif arr[y][x] == arr[y][x+1]:
                    arrr[y][x] = arrr[y][x+1]
                else:
                    arrr[y][x] = False

            if y > 0:
                if arr[y][x] > arr[y-1][x]:
                    arru[y][x] = True
                elif arr[y][x] == arr[y-1][x]:
                    arru[y][x] = arru[y-1][x]
                else:
                    arru[y][x] = False

            if y < m-1:
                if arr[y][x] > arr[y+1][x]:
                    arrd[y][x] = True
                elif arr[y][x] == arr[y+1][x]:
                    arrd[y][x] = arrd[y+1][x]
                else:
                    arrd[y][x] = False

    correct = True
    for y in range(m):
        for x in range(n):
            if ((arru[y][x] and arrd[y][x]) or
                (arrl[y][x] and arrr[y][x])):
                continue
            else:
                correct = False
                break

        if not correct:
            break

    print "Case #%d: %s" % (i + 1, "YES" if correct else "NO")

