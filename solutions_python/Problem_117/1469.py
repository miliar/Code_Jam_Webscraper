import sys
input = open(sys.argv[1], 'r')

for i in range(int(input.readline())):
    n, m = [int(x) for x in input.readline().split(' ')]

    lawn = []
    for _ in range(n):
        lawn.append([int(j) for j in input.readline().strip().split(' ')])

    result = True
    def maxForCol(col):
        res = -1
        for x in range(n): res = max(res, int(lawn[x][col]))
        return res

    def maxForRow(row):
        res = -1
        for x in range(m): res = max(res, int(lawn[row][x]))
        return res

    col0Max = maxForCol(0)
    def checkRow(row):
        curMax = lawn[row][0]

        h = lawn[row][0]
        if h < col0Max and h < maxForRow(row): return False

        for y in range(1, m):
            h = lawn[row][y]
            if h < curMax and maxForCol(y) > h: # and maxForCol(y-1) != curMax:
                return False
            curMax = max(curMax, h)

        return True

    for x in range(n):
        if not checkRow(x): result = False; break;

    print('Case #{}: {}'.format(i+1, 'YES' if result else 'NO'))
