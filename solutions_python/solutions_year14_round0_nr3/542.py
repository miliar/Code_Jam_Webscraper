import sys


def solve():
    t = int(sys.stdin.readline().strip())
    for test_case in xrange(0, t):
        r, c, m = map(int, sys.stdin.readline().strip().split(' '))

        def getNumber(field, x, y):
            if x < 0 or x >= r or y < 0 or y >= c:
                return -1
            res = 0
            if x > 0 and y > 0 and field[x - 1][y - 1] == '*': res += 1
            if x > 0 and field[x - 1][y] == '*': res += 1
            if x > 0 and y < c - 1 and field[x - 1][y + 1] == '*': res += 1
            if y > 0 and field[x][y - 1] == '*': res += 1
            if y < c - 1 and field[x][y + 1] == '*': res += 1
            if x < r - 1 and y > 0 and field[x + 1][y - 1] == '*': res += 1
            if x < r - 1 and field[x + 1][y] == '*': res += 1
            if x < r - 1 and y < c - 1 and field[x + 1][y + 1] == '*': res += 1
            return str(res)

        def inRowLimits(x):
            return x >= 0 and x < r

        def inColumnLimits(x):
            return x >= 0 and x < c

        def dfs(field, visited):
            for i in xrange(0, r):
                for j in xrange(0, c):
                    if field[i][j] == '0' and (i, j) not in visited:
                        if inRowLimits(i - 1):
                            if inColumnLimits(j - 1):
                                field[i - 1][j - 1] = getNumber(field, i - 1, j - 1)
                            field[i - 1][j] = getNumber(field, i - 1, j)
                            if inColumnLimits(j + 1):
                                field[i - 1][j + 1] = getNumber(field, i - 1, j + 1)

                        if inColumnLimits(j - 1):
                            field[i][j - 1] = getNumber(field, i, j - 1)
                        if inColumnLimits(j + 1):
                            field[i][j + 1] = getNumber(field, i, j + 1)

                        if inRowLimits(i + 1):
                            if inColumnLimits(j - 1):
                                field[i + 1][j - 1] = getNumber(field, i + 1, j - 1)
                            field[i + 1][j] = getNumber(field, i + 1, j)
                            if inColumnLimits(j + 1):
                                field[i + 1][j + 1] = getNumber(field, i + 1, j + 1)
                        visited.append((i, j))
            return visited

        def checkPosition(field, x, y):
            field2 = []
            for row in field:
                field2.append(list(row))
            field2[x][y] = getNumber(field, x, y)
            visited, visited2 = [], []
            while True:
                visited = dfs(field2, visited)
                if len(visited) == len(visited2):
                    break
                visited2 = list(visited)

            for i in xrange(0, r):
                for j in xrange(0, c):
                    if field2[i][j] == '.':
                        return False
            return True

        def checkPositions(mines):
            field = []
            for i in xrange(0, r):
                field.append(['.']*c)
            for mine in mines:
                field[mine[0]][mine[1]] = '*'
            for i in xrange(0, r):
                for j in xrange(0, c):
                    if field[i][j] != '*':
                        if checkPosition(field, i, j):
                            field[i][j] = 'c'
                            print >> sys.stdout, "Case #%s:" % (test_case + 1)
                            for i in xrange(0, r):
                                print >> sys.stdout, "".join(field[i])
                            return True
            return False

        def canBeNext(current, x, y):
            if len(current) > 0:
                if current[0] != (0, 0):
                    return False
                return x > current[-1][0] or (x - current[-1][0] == 0 and y > current[-1][1])
            return True

        def deep(current, checks):
            if len(current) == m:
                checks.append(0)
                if checkPositions(current):
                    return True
                return False
            for i in xrange(0, r):
                for j in xrange(0, c):
                    if (i, j) not in current and len(checks) < 1000 and canBeNext(current, i, j):
                        if deep(current + [(i, j)], checks):
                            return True
            return False

        if (m > r * c - 2 * (2 if r > 1 and c > 1 else 1) and m != r * c - 1) or not deep([], []):
            print >> sys.stdout, "Case #%s:" % (test_case + 1)
            print >> sys.stdout, "Impossible"


if __name__ == "__main__":
    solve()