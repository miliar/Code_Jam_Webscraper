import sys


def getline():
    return sys.stdin.readline().strip()

getints = lambda: map(int, getline().split(' '))

cases, = getints()

for case in xrange(cases):
    possible = True

    n, m = getints()

    lawn = []
    row_max = [0] * n
    col_max = [0] * m

    for x in xrange(n):
        row = getints()
        lawn.append(row)
        row_max[x] = max(row)

        for i, height in enumerate(row):
            col_max[i] = max(col_max[i], height)

    for row in xrange(n):
        for col in xrange(m):
            height = lawn[row][col]
            if row_max[row] > height and col_max[col] > height:
                possible = False
                break
        if not possible:
            break

    result = 'YES' if possible else 'NO'

    print "Case #{case}: {result}".format(case=case + 1, result=result)
