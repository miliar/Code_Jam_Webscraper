import os
import sys


def process_file(in_name, out_name):
    with open(in_name, 'r') as fin:
        with open(out_name, 'w') as fout:
            def read():
                while True:
                    l = fin.readline()
                    if len(l) == 0:
                        raise Exception('EOF')
                    l = l.strip('\n')
                    if len(l):
                        return l

            def write(*args):
                fout.write(' '.join(map(str, args)))

            t = int(fin.readline())
            for i in range(t):
                write(f'Case #{i + 1}:\n')
                solve(read, write)


def solve(read, write):
    r, c = map(int, read().split())
    grid = []
    for i in range(r):
        grid.append(list(read()))

    for i in range(r):
        char = '?'
        for j in range(c):
            if grid[i][j] != '?':
                char = grid[i][j]
                break
        if char == '?':
            continue
        for j in range(c):
            if grid[i][j] == '?':
                grid[i][j] = char
            else:
                char = grid[i][j]

    for j in range(c):
        char = '?'
        for i in range(r):
            if grid[i][j] != '?':
                char = grid[i][j]
                break
        if char == '?':
            print('error')
            continue

        for i in range(r):
            if grid[i][j] == '?':
                grid[i][j] = char
            else:
                char = grid[i][j]

    # printgrid(grid)
    for l in grid:
        write(''.join(l) + '\n')


def printgrid(grid):
    for l in grid:
        print(''.join(l))


if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 2:
        in_name = args[1]
        out_name = args[2] if len(args) == 3 else (
            (in_name[:-3] if in_name.endswith('.in')
             else in_name) + '.out')
        process_file(in_name, out_name)
    else:
        for in_name in os.listdir():
            if in_name.endswith('.in'):
                out_name = in_name[:-3] + '.out'
                process_file(in_name, out_name)
