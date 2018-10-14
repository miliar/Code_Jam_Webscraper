
from collections import deque

def get_line():
    return raw_input().strip()
     
formatIntList = lambda s: list(map(int,s.split(' ')))

def standard_input():
    count = int(get_line())
    for i in range(count):
        case = formatIntList(get_line())
        yield (i+1,case)

def neighbors(grid, current):
    mn,fn = list(), list()
    i,j = current
    for di in range(-1,2):
        if i+di < 0 or i+di >= len(grid):
            continue
        row = grid[i+di]
        for dj in range(-1,2):
            if di == 0 and dj == 0:
                continue
            if j+dj < 0 or j+dj >= len(row):
                continue
            c = row[j+dj]
            if c == '*':
                mn.append((i+di,j+dj))
            elif c == '.':
                fn.append((i+di,j+dj))
    return mn,fn

def test_case(R,C,M,grid):
    startindex = set((i,j) for i in range(R) \
        for j in range(C) if grid[i][j] == 'c').pop()
    q = deque()
    q.append(startindex)
    count = 0
    # print '\n'.join(''.join(lst) for lst in grid)
    while len(q) > 0:
        i,j = q.popleft()
        if grid[i][j] == '^':
            continue
        grid[i][j] = '^'
        count += 1
        mn, fn = neighbors(grid, (i,j))
        if len(mn) == 0:
            for x in fn:
                q.append(x)
    # print '\n'.join(''.join(lst) for lst in grid)
    for (i,j) in ((i,j) for i in range(R) \
        for j in range(C)):
            if grid[i][j] == '^':
                grid[i][j] = '.'
    grid[startindex[0]][startindex[1]] = 'c'
    return count == R*C - M

def empty_grid(R,C):
    result = list()
    for i in range(R):
        result.append(C*['.'])
    return result
    
def create_grid(R,C,binvec):
    grid = empty_grid(R,C)
    for i in range(R*C):
        if (1 << i) & binvec > 0:
            grid[i/C][i%C] = '*'
    return grid

def bitcount(N):
    count = 0
    while N > 0:
        count += N & 1
        N >>= 1
    return count
    
def nextVector(v):
    t = (v | (v - 1)) + 1;  
    w = t | ((((t & -t) / (v & -v)) >> 1) - 1)
    return w

def generate_grids(R,C,M):
    N = R*C
    binvec = (1 << M) - 1
    while binvec < (1 << N):
        # print bin(binvec)
        for j in range(0,N):
            if (1 << j) & binvec > 0:
                continue
            grid = create_grid(R,C,binvec)
            grid[j/C][j%C] = 'c'
            yield grid
        binvec = nextVector(binvec)

   
def handle_case(case):
    R,C,M = tuple(case)
    if R == 5 and C >= 4 and R*C - M in [2,3,5,7]:
        return 'Impossible'
    if C == 5 and R >= 4 and R*C - M in [2,3,5,7]:
        return 'Impossible'
    for grid in generate_grids(R,C,M):
        if test_case(R,C,M,grid):
            return '\n'.join(''.join(lst) for lst in grid)
    return 'Impossible'

def main():
    for i,case in standard_input():
        print "Case #%d:\n%s" %(i,handle_case(case).rstrip())       

if __name__ == '__main__':
    main()