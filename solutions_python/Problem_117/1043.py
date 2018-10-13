from sys import argv

script, filename = argv

f = open(filename)

T = int(f.readline())


def check(array, x, y):
    res = [[0]*y for i in range(x)]

    for i in range(x):
        m = 0
        for j in range(y):
            if array[i][j] > m:
                m = array[i][j]
        for j in range(y):
            if array[i][j] == m:
                res[i][j] = 1

    for j in range(y):
        m = 0
        for i in range(x):
            if array[i][j] > m:
                m = array[i][j]
        for i in range(x):
            if array[i][j] == m:
                res[i][j] = 1

    for i in range(x):
        for j in range(y):
            if res[i][j] == 0:
                return 'NO'

    return 'YES'
for t in range(T):
    (x, y) = map(int, f.readline().split())

    array = []
    for i in range(x):
        array.append(map(int, f.readline().split()))

    print 'Case #{0}: {1}'.format(t + 1, check(array, x, y))


f.close()
