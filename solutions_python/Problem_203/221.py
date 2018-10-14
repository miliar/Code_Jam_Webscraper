f_in = open('A-large.in')
f_out = open('A-large.out', 'w')

N = int(f_in.readline())

def prettyprint(grid):
    for r in grid:
        print ''.join([str(x) for x in r])

def solve():
    R, C = [int(x) for x in f_in.readline().rstrip().split()]
    grid = []
    q = []  # unexpanded letters
    initial_loc = {}  # map of letter to initial location in grid
    for rn in range(R):
        l = list(f_in.readline().rstrip())
        grid.append(l)
        for cn, initial in enumerate(l):
            if initial != '?':
                initial_loc[initial] = (rn, cn)
                q.append(initial)
    # prettyprint(grid)
    # print q, initial_loc

    # Greedily expand each letter as much as possible;
    # first across, then down.
    for x in q:
        orig_r, orig_c = initial_loc[x]
        # Expand across
        left, right = orig_c, orig_c  # Note: both are inclusive
        # goin right
        for cn in range(orig_c+1, C):
            if grid[orig_r][cn] == '?':
                grid[orig_r][cn] = x
                right += 1
            else:
                break
        # goin left
        for cn in range(orig_c-1, -1, -1):
            if grid[orig_r][cn] == '?':
                grid[orig_r][cn] = x
                left -= 1
            else:
                break

        # print 'left n right for ',x,  left, right
        # prettyprint(grid)

        # Expand vertically
        # goin down
        for rn in range(orig_r+1, R):
            # CAREFUL OF INDEXING HERE
            if all([y == '?' for y in grid[rn][left:right+1]]):
                for cn in range(left, right+1):
                    grid[rn][cn] = x
            else:
                break
        # goin up
        for rn in range(orig_r-1, -1, -1):
            # CAREFUL OF INDEXING HERE
            if all([y == '?' for y in grid[rn][left:right+1]]):
                for cn in range(left, right+1):
                    grid[rn][cn] = x
            else:
                break
        # print 'up and down for ',x
        # prettyprint(grid)
    return '\n' + '\n'.join(''.join(r) for r in grid)

for case in range(1, N+1):
    out = 'Case #{}: {}\n'.format(case, solve())
    print out
    f_out.write(out)




f_in.close()
f_out.close()
