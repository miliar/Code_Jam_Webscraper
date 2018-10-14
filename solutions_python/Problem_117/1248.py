
def solve(lawn, rows, cols):
    row_maxes = [max(row) for row in lawn]
    col_maxes = [max(col) for col in zip(*lawn)]
    return all(
        lawn[rowno][colno] in (
            row_maxes[rowno],
            col_maxes[colno]
        )
        for rowno in xrange(rows)
        for colno in xrange(cols)
    )

def main():
    t = int(raw_input().strip())
    for case in xrange(1,t+1):
        rows, cols = map(int,raw_input().split())
        lawn = [map(int,raw_input().split()) for row in xrange(rows)]
        print "Case #{}: {}".format(
                case,
                "YES" if solve(lawn,rows,cols) else "NO")

if __name__=="__main__":
    main()
