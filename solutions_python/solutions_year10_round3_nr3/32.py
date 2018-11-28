import sys
from collections import defaultdict

T = int(sys.stdin.readline())


def print_grid(grid):
    colours = {-1: ' ', 0: '#', 1: '-'}
    for i, l in enumerate(grid):
        for j in l:
            sys.stderr.write(colours[j])
        sys.stderr.write('\n')
    sys.stderr.write('\n')


def b2b(bits):
    soddit = [
      '0000', '0001', '0010', '0011',
      '0100', '0101', '0110', '0111',
      '1000', '1001', '1010', '1011',
      '1100', '1101', '1110', '1111',
    ]
    
    grid = []
    for row in bits:
        grid.append([])
        for c in row:
            group = map(int, soddit[int(c, 16)])
            grid[-1].extend(group)
    return grid

def is_valid_line(grid, m, n, length):
    if m+length > len(grid[0]) or n > len(grid):
        return False
    
    for cell in range(m+1, m+length):
        if grid[n][cell] != 1-grid[n][cell-1]:
            return False
    return True

def largest_at(grid, m, n):
    if grid[n][m] < 0:
        return 0
    
    result = 1
    while True:
        if m+result > len(grid[0]) or n+result+1 > len(grid):
            break
        inc = 1
        if grid[n+result][m] != 1-grid[n+result-1][m]:
            break
        
        for line in range(result+1):
            if not is_valid_line(grid, m, n+line, result+1):
                inc = 0
                break
        
        if not inc:
            break
        
        result += 1
    
    return result

def remove_board(grid, m, n, size):
    for i in range(m, m+size):
        for j in range(n, n+size):
            grid[j][i] = -1

def solve2(grid):
    results = defaultdict(int)
    while True:
        grids = []
        
        for n, l in enumerate(grid):
            for m in range(len(l)):
                size = largest_at(grid, m, n)
                if not size:
                    continue
                grids.append((size, -n, -m))
        
        if not grids:
            break
        
        winnar = sorted(grids, reverse=True)[0]
        print>>sys.stderr, 'Removing grid of size %s at %s,%s' % (winnar[0], winnar[2], winnar[1])
        print_grid(grid)
        remove_board(grid, -winnar[2], -winnar[1], winnar[0])
        results[winnar[0]] += 1
    
    return results

def solve(grid):
    results = solve2(grid)
    answer = str(len(results)) + "\n"
    answer += "\n".join(["%s %s" % (s, n) for s, n in sorted(results.items(), reverse=True)])
    
    return answer

for i in range(T):
    # i = int(sys.stdin.readline())
    # s = sys.stdin.readline().strip('\n')
    # l = sys.stdin.readline().strip('\n').split()
    M, N = map(int, sys.stdin.readline().split())
    grid = []
    for j in range(M):
        grid.append(sys.stdin.readline().strip('\n'))
    print "Case #%s: %s" % (i+1, solve(b2b(grid)))
