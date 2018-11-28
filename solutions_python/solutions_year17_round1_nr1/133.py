
def solve(R, C, grid):
    for r in range(R):
        for c in range(C):
            x = grid[r][c]
            if x != '?':
                r_up = r - 1
                while r_up >= 0 and grid[r_up][c] == '?':
                    grid[r_up][c] = x
                    r_up -= 1
                if r + 1 < R and grid[r + 1][c] == '?':
                    grid[r + 1][c] = x
    # at this point, only whole columns will be left unfilled
    use_c = []
    for c in range(C):
        if grid[0][c] != '?':
            for r in range(R):
                use_c.append(grid[r][c])
            break
    for c in range(C):
        if grid[0][c] == '?':
            for r in range(R):
                grid[r][c] = use_c[r]
        else:
            use_c = []
            for r in range(R):
                use_c.append(grid[r][c])
    output = []
    for r in range(R):
        output.append(''.join(grid[r]))
    return '\n'.join(output)


if __name__ == "__main__":
    output = []
    fname = 'A-large'
    with open(fname + '.in') as f:
        inputs = [line.strip() for line in f]

    num_cases = int(inputs[0])
    line = [1]

    def next_line():
        text = inputs[line[0]]
        line[0] += 1
        return text

    for i in range(num_cases):
        R, C = map(int, next_line().split())
        grid = []
        for j in range(R):
            grid.append([c for c in next_line()])
        output.append("Case #%d:" % (i + 1))
        output.append(solve(R, C, grid))

    with open(fname + '.out', 'w') as f:
        f.write('\n'.join(output))
