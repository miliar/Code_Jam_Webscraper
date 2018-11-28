#import numpy as np 
from itertools import \
    product, \
    permutations, \
    combinations, \
    combinations_with_replacement
from functools import reduce, lru_cache
from math import floor,ceil,inf,sqrt

def solve(grid):
    grid = list(map(list, grid))
    R = len(grid); C = len(grid[0])
    
    # Row pass
    for i in range(R):
        current = '?'
        for j in range(C):
            if grid[i][j] == '?':
                grid[i][j] = current
            else:
                current = grid[i][j]

        current = '?'
        for j in range(C-1, -1, -1):
            if grid[i][j] == '?':
                grid[i][j] = current
            else:
                current = grid[i][j]

    # Safety check
    for line in grid:
        if '?' in line:
            assert(all(s == '?' for s in line))

    # Column pass
    for j in range(C):
        current = '?'
        for i in range(R):
            if grid[i][j] == '?':
                grid[i][j] = current
            else:
                current = grid[i][j]

        current = '?'
        for i in range(R-1, -1, -1):
            if grid[i][j] == '?':
                grid[i][j] = current
            else:
                current = grid[i][j]

    # Translate to string
    return list(map(lambda x: ''.join(x), grid))


            

    
                
if __name__ == '__main__':
    import sys,re
    data = iter(sys.stdin.read().splitlines())
    T = int(next(data))
    for (case_num, case) in enumerate(data):
        R,C = map(int, case.split())
        
        grid = []
        for _ in range(R):
            grid.append(list(next(data)))
            
        print('Case #{}:'.format(case_num+1))
        for line in solve(grid):
          print(line)
              
