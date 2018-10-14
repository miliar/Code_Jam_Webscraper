#!/usr/bin/env 
import sys
import fileinput


# Case #1: 7
# Case #2: Bad magician!
# Case #3: Volunteer cheated!

BAD = 'Bad magician!'
CHEATED = 'Volunteer cheated!'
EXAMPLES_PER_CASE = 2
GRID_ROWS = 4

def do_case(f):
    sets = []
    for i in xrange(EXAMPLES_PER_CASE):
        ans = int(f.readline())
        grid = []
        for j in xrange(0,GRID_ROWS):
            grid.append(f.readline().split())
        sets.append(set(grid[ans - 1]))
    s = sets[0] & sets[1]
    x = len(s)
    if x == 0:
        return CHEATED
    elif x == 1:
        return s.pop()
    else:
        return BAD

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    for t in xrange(1,T+1):
        print 'Case #{}: {}'.format(t, do_case(f))

if __name__ == '__main__':
    main()    
