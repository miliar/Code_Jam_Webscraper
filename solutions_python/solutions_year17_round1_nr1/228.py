def expand(row):
    to_update = []
    fixed = 0

    for j in range(len(row)):
        if row[j] == '?':
            to_update.append(j)
        else:
            for x in to_update:
                row[x] = row[j]
                fixed += 1

            to_update = []
            while j + 1 < len(row) and row[j + 1] == '?':
                row[j + 1] = row[j]
                j += 1
                fixed += 1

    return row, fixed

def solve(grid):
    missing = 0
    for x in grid:
         missing += x.count('?')

    while missing > 0:
        any_change = missing
        for i in range(len(grid)):
            (tmp_row, fixed) = expand(grid[i])
            grid[i] = tmp_row
            missing -= fixed

        if missing == any_change:
            for i in range(len(grid)):
                if len([x for x in grid[i] if x == '?']) != len(grid[0]):
                    continue
                if i - 1 >= 0 and len([x for x in grid[i - 1] if x != '?']) > 0:
                    grid[i] = grid[i - 1]
                    missing -= len(grid[0])
                elif i + 1 < len(grid) and len([x for x in grid[i + 1] if x != '?']) > 0:
                    grid[i] = grid[i + 1]
                    missing -= len(grid[0])

    grid = map(lambda x: "".join(x), grid)
    return "\n".join(grid)


def main():
    t = int(input())
    for i in range(1, t + 1):
        r, c = [int(s) for s in input().split(" ")]
        s = []
        for j in range(r):
            s.append(list(input()))
        print(f"Case #{i}:\n{solve(s)}")


if __name__ == "__main__": main()