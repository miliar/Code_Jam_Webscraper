import sys


def solve(instream):
    rows, cols = [int(x) for x in instream.readline().strip().split(" ")]
    lawn = [[int(x) for x in instream.readline().strip().split(" ")]
            for row in range(rows)]

    h_highest = [max(row) for row in lawn]
    v_highest = [max(row[coli] for row in lawn) for coli in range(cols)]

    return "YES" if all(
        all(lawn[rowi][coli] >= h_highest[rowi] or
            lawn[rowi][coli] >= v_highest[coli]
            for coli in range(cols))
        for rowi in range(rows)
    ) else "NO"


def run():
    cases = int(sys.stdin.readline().strip())
    for i in range(cases):
        print("Case #{}: {}".format(i + 1, solve(sys.stdin)))

if __name__ == "__main__":
    run()
