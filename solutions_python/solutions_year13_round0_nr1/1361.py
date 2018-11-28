import collections

T = int(raw_input())
for t in range(T):
    grid = []
    for i in range(4):
        grid.append(raw_input().strip())
    try:
        raw_input()
    except:
        pass

    def result(cts):
        if cts['X'] == 4 or (cts['X'] == 3 and cts['T'] == 1):
            return 'X'
        if cts['O'] == 4 or (cts['O'] == 3 and cts['T'] == 1):
            return 'O'
        return None

    def check_row(r):
        cts = collections.defaultdict(int)
        for c in range(4):
            ch = grid[r][c]
            cts[ch] += 1
        return result(cts)

    def check_col(c):
        cts = collections.defaultdict(int)
        for r in range(4):
            ch = grid[r][c]
            cts[ch] += 1
        return result(cts)

    def check_diags():
        cts = collections.defaultdict(int)
        for i in range(4):
            ch = grid[i][i]
            cts[ch] += 1
        res = result(cts)
        if res is not None:
            return res
        cts = collections.defaultdict(int)
        for i in range(4):
            ch = grid[3 - i][i]
            cts[ch] += 1
        return result(cts)

    def completed():
        for i in range(4):
            for j in range(4):
                if grid[i][j] == '.':
                    return False
        return True

    res = None
    for r in range(4):
        res = check_row(r)
        if res is not None:
            break

    if res is None:
        for c in range(4):
            res = check_col(c)
            if res is not None:
                break

        if res is None:
            res = check_diags()

    c = completed()
    if res is None:
        if c:
            res_str = 'Draw'
        else:
            res_str = 'Game has not completed'
    else:
        res_str = '%s won' % res

    print 'Case #%s: %s' % (t + 1, res_str)
