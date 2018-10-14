import sys

def fillLine(cake, row):
    unfilledStart = 0
    unfilledEnd = 0
    lastLet = None
    lastLetPos = None

    for j in range(len(cake[row])):
        if cake[row][j] != '?':
            lastLet = cake[row][j]
            lastLetPos = j
            for k in range(j - 1, -1, -1):
                if cake[row][k] == '?':
                    cake[row][k] = cake[row][j]
                else:
                    break
    if lastLet == None:
        return False
    else:
        for k in range(lastLetPos + 1, len(cake[row])):
            cake[row][k] = lastLet
        return True

def copyLine(cake, source, dest):
    cake[dest] = cake[source]

def cakey(cake):
    unfilledStart = 0
    unfilledEnd = 0
    for i in range(len(cake)):
        # print i, unfilledStart, unfilledEnd
        if fillLine(cake, i):
            for j in range(unfilledStart, unfilledEnd):
                copyLine(cake, i, j)
            unfilledStart = i + 1
        else:
            unfilledEnd = i + 1

    for j in range(unfilledStart, unfilledEnd):
        copyLine(cake, unfilledStart - 1, j)

    return '\n'.join(map(lambda row: ''.join(row), cake))

if __name__ == '__main__':
    test = open(sys.argv[1], 'r')
    for i in range(int(test.readline().strip())):
        R, C = test.readline().strip().split()
        cake = []
        for j in range(int(R)):
            cake.append(list(test.readline().strip()))
        print('Case #' + str(i + 1) + ': ' + '\n' + str(cakey(cake)))
