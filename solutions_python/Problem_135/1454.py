#!/usr/bin/env python3
import sys

def main(argv=sys.argv):
    fin, fout = argv[1:3]
    with open(fin) as f, open(fout, 'w') as g:
        T = int(f.readline().strip())
        for i in range(1, T+1):
            guess = int(f.readline().strip())
            grid = []
            for _ in range(4):
                grid.append(tuple(map(int, f.readline().strip().split())))
            candidates = set(grid[guess-1])
            guess = int(f.readline().strip())
            grid = []
            for _ in range(4):
                grid.append(tuple(map(int, f.readline().strip().split())))

            candidates &= set(grid[guess-1])
            if len(candidates) == 0:
                result = 'Volunteer cheated!'
            elif len(candidates) == 1:
                result = candidates.pop()
            else:
                result = 'Bad magician!'
            g.write("Case #{}: {}\n".format(i, result))

if __name__ == "__main__":
    status = main()
    sys.exit(status)
