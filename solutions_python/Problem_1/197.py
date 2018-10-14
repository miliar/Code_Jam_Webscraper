import sys
import fileinput

MAX = 10000000

def solve(engines, queries):
    if len(queries) == 0:
        return 0

    results = []
    m = {}

    grid = []
    for i in range(0, len(engines)):
        m[engines[i]] = i
        tmp = []
        for j in range(0, len(queries)):
            tmp.append(MAX)
        grid.append(tmp)

    q = map(lambda x:  m[x], queries)

    for i in range(0, len(engines)):
        if i != q[0]:
            grid[i][0] = 0

    for i in range(1, len(q)):
        for j in range(0, len(engines)):
            prev = []
            for k in range(0, len(engines)):
                if k != j:
                    prev.append(1+grid[k][i-1])
                else:
                    prev.append(grid[k][i-1])

            if j != q[i]:
                grid[j][i] = min(prev)

    results = []
    for j in range(0, len(engines)):
        results.append(grid[j][len(q)-1])

    return min(results)

if __name__ == '__main__':
    lines = fileinput.input(sys.argv[1])
    num = int(lines.readline())
    for i in range(1, num+1):
        num_engines = int(lines.readline())
        engines = []
        for j in range(0, num_engines):
            engines.append(lines.readline().rstrip())

        num_queries = int(lines.readline())
        queries = []
        for j in range(0, num_queries):
            queries.append(lines.readline().rstrip())

        out = solve(engines, queries)

        print 'Case #%d: %s' % (i, out)


