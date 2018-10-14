import sys

def run(): # {{{
    inp=sys.argv[1]
    outp="%s.out" % inp.split(".")[0]

    with open(inp, 'r') as _file, open(outp, 'w') as out:
        _cases = int(_file.readline())
        for _case in range(_cases):
            print("Solving case %s" % (_case+1))
            r, c = tuple([int(x) for x in _file.readline().split(" ")])
            grid = []
            for i in range(r):
                grid.append(_file.readline()[:-1])
            out.write("Case #%s: %s\n" % (_case+1, _format(solve(r, c, grid))))
# }}}

def _format(result):
    return result

def free(grid, rows, cols):
    for i in rows:
        for j in cols:
            if grid[i][j] != ".": return False
    return True

def solve(r, c, grid):
    res = 0
    for i in range(r):
        for j in range(c):
            cell = grid[i][j]
            if cell == ".": continue
            free_right = free(grid, [i], range(j+1, c))
            free_left = free(grid, [i], range(j))
            free_up = free(grid, range(i), [j])
            free_down = free(grid, range(i+1, r), [j])
            if cell != "." and free_right and free_left and free_up and free_down:
                return "IMPOSSIBLE"
            if cell == ">" and free_right: res += 1
            if cell == "<" and free_left: res += 1
            if cell == "^" and free_up: res += 1
            if cell == "v" and free_down: res += 1
    return res

run()
