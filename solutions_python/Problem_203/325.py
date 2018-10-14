#!/usr/bin/env python

import sys

def solve(*args):
    (R,C,grid) = args
    
    all_q = "?" * C
    last_row = 0
    
    for index in xrange(R):
        # first pass skip allqs
        if grid[index] == all_q:
            continue
        
        if last_row == 0:
            last_row = index
        
        last_char = ''
        for l in grid[index]:
            if l != "?":
                last_char = l
                break
        
        #print grid
        
        for lindex, l in enumerate(grid[index]):
            #print lindex, grid,
            if l == '?':
                grid[index] = grid[index][:lindex] + last_char + grid[index][lindex+1:]
            else:
                last_char = l
            #print grid
                
        #print grid
        
    for index in xrange(R):
        # first pass skip allqs
        if grid[index] == all_q:
            grid[index] = grid[last_row]
        else:
            last_row = index

    return "\n{}".format("\n".join(grid))

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
        R, C = map(int, sys.stdin.readline().split())
        grid = []
        for r in xrange(R):
            grid.append(sys.stdin.readline().strip())
        result = solve(R, C, grid)
        print "Case #%d: %s" % (caseNumber, result)
       
if __name__ == '__main__':
    main()


