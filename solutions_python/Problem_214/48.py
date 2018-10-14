#!/usr/bin/python

def getHorizontal(R, C, grid, r_s, c_s):
    horizontal_range = set()
    dx = -1
    dy = 0
    r, c = r_s, c_s - 1
    while r >= 0 and c >= 0 and r < R and c < C:
        cell = grid[r][c]
        if cell == '#':
            break
        elif cell == '-' or cell == '|':
            return None
        elif cell == '/':
            if dx == 0:
                dx = -dy
                dy = 0
            else:
                dy = -dx
                dx = 0
        elif cell == '\\':
            if dx == 0:
                dx = dy
                dy = 0
            else:
                dy = dx
                dx = 0
        else:
            horizontal_range.add((r, c))
        r, c = r + dy, c + dx
    dx = 1
    dy = 0
    r, c = r_s, c_s + 1
    while r >= 0 and c >= 0 and r < R and c < C:
        cell = grid[r][c]
        if cell == '#':
            break
        elif cell == '-' or cell == '|':
            return None
        elif cell == '/':
            if dx == 0:
                dx = -dy
                dy = 0
            else:
                dy = -dx
                dx = 0
        elif cell == '\\':
            if dx == 0:
                dx = dy
                dy = 0
            else:
                dy = dx
                dx = 0
        else:
            horizontal_range.add((r, c))
        r, c = r + dy, c + dx
    return horizontal_range

def getVertical(R, C, grid, r_s, c_s):
    vertical_range = set()
    dx = 0
    dy = -1
    r, c = r_s - 1, c_s
    while r >= 0 and c >= 0 and r < R and c < C:
        cell = grid[r][c]
        if cell == '#':
            break
        elif cell == '-' or cell == '|':
            return None
        elif cell == '/':
            if dx == 0:
                dx = -dy
                dy = 0
            else:
                dy = -dx
                dx = 0
        elif cell == '\\':
            if dx == 0:
                dx = dy
                dy = 0
            else:
                dy = dx
                dx = 0
        else:
            vertical_range.add((r, c))
        r, c = r + dy, c + dx
    dx = 0
    dy = 1
    r, c = r_s + 1, c_s
    while r >= 0 and c >= 0 and r < R and c < C:
        cell = grid[r][c]
        if cell == '#':
            break
        elif cell == '-' or cell == '|':
            return None
        elif cell == '/':
            if dx == 0:
                dx = -dy
                dy = 0
            else:
                dy = -dx
                dx = 0
        elif cell == '\\':
            if dx == 0:
                dx = dy
                dy = 0
            else:
                dy = dx
                dx = 0
        else:
            vertical_range.add((r, c))
        r, c = r + dy, c + dx
    return vertical_range

# def rec(coverageCount, grid, shooter, h_range, v_range):
    

def go(R, C, grid):
    empties = set()
    shooters = []
    for r in range(R):
        for c in range(C):
            cell = grid[r][c]
            if cell == '.':
                empties.add((r, c))
            elif cell == '-' or cell == '|':
                shooters.append((r, c))
    ranges = {}
    coverage = set()
    for r_s, c_s in shooters:
        h_range = getHorizontal(R, C, grid, r_s, c_s)
        v_range = getVertical(R, C, grid, r_s, c_s)
        if h_range is None and v_range is None:
            return None
        elif h_range is not None and v_range is None:
            coverage.update(h_range)
            empties = empties.difference(h_range)
            grid[r_s][c_s] = '-'
        elif h_range is None and v_range is not None:
            coverage.update(v_range)
            empties = empties.difference(v_range)
            grid[r_s][c_s] = '|'
        else:
            if not h_range:
                grid[r_s][c_s] = '|'
                empties = empties.difference(v_range)
            elif not v_range:
                grid[r_s][c_s] = '-'
                empties = empties.difference(h_range)
            else:
                intersection = h_range.intersection(v_range)
                h_range = h_range.difference(intersection)
                v_range = v_range.difference(intersection)
                empties = empties.difference(intersection)
                coverage.update(h_range)
                coverage.update(v_range)
                ranges[(r_s, c_s)] = (h_range, v_range)
    if len(empties) == 0:
        return grid
    if empties.difference(coverage):
        return None
    for s, (h, v) in ranges.items():
        ranges[s] = (h.intersection(empties), v.intersection(empties))
    
#     print(empties)
#     print(ranges)
    numEmpties = len(empties)
    ranges = list(ranges.items())
    def test(orients):
        coverage = set()
        for i, o in enumerate(orients):
            coverage.update(ranges[i][1][o])
        return len(coverage) == len(empties)
    
    for i in range(2**len(ranges)):
        orients = []
        for j in range(len(ranges)):
            orients.append(i % 2)
            i //= 2
        if test(orients):
            for i, o in enumerate(orients):
                r, c = ranges[i][0]
                grid[r][c] = '|' if o else '-'
            return grid
    return None

def printGrid(grid):
    for r in grid:
        print(''.join(r))

T = int(raw_input())
for t in range(T):
    R, C = map(int, raw_input().split())
    grid = []
    for i in range(R):
        grid.append(list(raw_input().strip()))
    
    result = go(R, C, grid)
    print("Case #%d: %s" % (t + 1, 'POSSIBLE' if result else 'IMPOSSIBLE'))
    if result:
        printGrid(result)
    