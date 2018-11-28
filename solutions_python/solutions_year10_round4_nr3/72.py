from pprint import pprint

def mk_empty_grid(side):
    grid = []
    for _ in xrange(side):
        grid.append([0] * side)
    return grid

def mk_grid(rectangles, side):
    grid = mk_empty_grid(side)
    for X1, Y1, X2, Y2 in rectangles:
        for x in xrange(X1 - 1, X2):
            for y in xrange(Y1 - 1, Y2):
                grid[y][x] = 1
#     pprint(grid)
    return grid

def find_max(rectangles):
    max_x = 0
    max_y = 0
    for X1, Y1, X2, Y2 in rectangles:
        if X2 > max_x: max_x = X2
        if Y2 > max_y: max_y = Y2
    return max(max_x, max_y)


def step(grid, size):
    new_grid = mk_empty_grid(size)
    n = 0

    def west(x, y):
        return grid[y][x - 1] if x > 0 else 0

    def north(x, y):
        return grid[y - 1][x] if y > 0 else 0

#     def place(x, y):
#         new_grid[y][x] = 1
#         global n
#         n = n + 1

    for y in xrange(size):
        for x in xrange(size):
            if grid[y][x]:
                # bacteria
                if not west(x, y) and not north(x, y):
                    # die
                    pass
                else:
                    new_grid[y][x] = 1
                    n += 1
#                     place(x, y)
            else:
                # no bacteria
                if west(x, y) and north(x, y):
                    new_grid[y][x] = 1
                    n += 1
#                     place(x, y)

#     pprint(new_grid)
#     print n
    return new_grid, n

def solve(rectangles):
    side = find_max(rectangles)
    grid = mk_grid(rectangles, side)
    T = 0
    while True:
        grid, n = step(grid, side)
        T += 1
        if n == 0:
            break
    return T

if __name__ == '__main__':
    C = input()
    for i in xrange(C):
        R = input()
        rectangles = []
        for _ in xrange(R):
            r = tuple(int(x) for x in raw_input().split())
            rectangles.append(r)
        T = solve(rectangles)
        print 'Case #%d: %d' % (i + 1, T)

