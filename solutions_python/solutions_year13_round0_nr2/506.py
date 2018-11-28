import sys, itertools

def mow(lawn, n, m):
    mota = sorted(set(itertools.chain.from_iterable(lawn)))
    for j in mota:
        todo = list()
        nonoRow = set()
        nonoCol = set()
        for r in range(n):
            for c in range(m):
                J = lawn[r][c]
                if (j == J):
                    todo.append((r, c))
                elif (j < J):
                    nonoRow.add(r)
                    nonoCol.add(c)
        for (r, c) in todo:
            if r in nonoRow and c in nonoCol:
                return 'NO'
    return 'YES'

s = sys.stdin
T = int(s.readline())
for t in range(T):
    n, m = map(int, s.readline().split())
    sys.stdout.write("Case #{}: {}\n".format(t + 1,
        mow([map(int, s.readline().split()) for _ in range(n)], n, m)))
