import sys
inp = sys.stdin.readlines()

cases = int(inp.pop(0))

for case in range(1, cases + 1):
    line = inp.pop(0).strip()
    R, C = line.split()
    R = int(R)
    C = int(C)
    rows = []
    for _ in range(R):
        rows.append(list(inp.pop(0).strip()))
    frow = None
    for r in range(R):
        empty = True
        fcell = None
        for c in range(C):
            if rows[r][c] != '?':
                fcell = rows[r][c]
                for ci in range(c):
                    if rows[r][ci] is None:
                        rows[r][ci] = fcell
                empty = False
            elif fcell is not None:
                rows[r][c] = fcell
            else:
                rows[r][c] = None
        if empty:
            rows[r] = frow
        else:
            frow = rows[r]
            for ri in range(r):
                if rows[ri] is None:
                    rows[ri] = frow[:]
    try:
        result = "\n" + "\n".join("".join(r) for r in rows)
    except:
        print rows
        raise
    print 'Case #{}: {}'.format(case, result)
