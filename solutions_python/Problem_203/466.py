import sys

def main():
    infile = sys.argv[1]
    with open(infile) as f, open(infile[:-2] + 'out', 'wb') as o:
        T = int(f.next())
        for case in xrange(T):
            R, C = map(int, f.next().split())
            grid = [list(f.next().strip()) for r in xrange(R)]
            fun(grid)
            o.write('Case #%d:\n' % (case + 1))
            o.write('\n'.join(''.join(row) for row in grid) + '\n')

def fun(grid):
    R, C = len(grid), len(grid[0])
    for r in xrange(R):
        row = grid[r]
        for c in xrange(C):
            if row[c] != '?':
                break
        else:
            continue
        last = 0
        while c < C:
            row[last:c] = [row[c] for _ in xrange(c-last)]
            c += 1
            last = c
            while c < C and row[c] == '?':
                c += 1
        row[last:c] = [row[last-1] for _ in xrange(c-last)]
    tocopy = []
    for r in xrange(R):
        if grid[r][0] == '?':
            tocopy.append(r)
        else:
            for i in tocopy:
                grid[i] = grid[r]
            tocopy = []
    for i in tocopy:
        grid[i] = grid[tocopy[0]-1]

if __name__ == '__main__':
    main()
