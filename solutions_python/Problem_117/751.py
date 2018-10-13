import sys


OUTCOMES = {False: "NO", True: "YES"}

def parse_row(row_str):
    return [int(x) for x in row_str.split()]

if __name__ == '__main__':
    TESTS = int(sys.stdin.readline())
    for z in range(1, TESTS + 1):
        n, m = [int(x) for x in sys.stdin.readline().split()]
        # Load the grid
        rows = []
        for i in range(n):
            rows.append(parse_row(sys.stdin.readline()))
        row_mins = [min(row) for row in rows]
        row_maxs = [max(row) for row in rows]
        col_mins = [min([rows[i][j] for j in range(m)]) for i in range(n)]
        col_maxs = [max([rows[i][j] for i in range(n)]) for j in range(m)]
        o = True
        for i in range(n):
            for j in range(m):
                if rows[i][j] < min(row_maxs[i], col_maxs[j]):
                    o = False
                    break
        print("Case #%d: %s" % (z, OUTCOMES[o]))
