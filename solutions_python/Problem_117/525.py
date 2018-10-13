'''
Created on April 13, 2013

@author: Anand
'''

import sys

sys.stdin = open('../BLawnmower.in')
sys.stdout = open('../BLawnmower.out', 'w')

def main():
    T = int(raw_input())
    for testcase in xrange(1, T + 1):
        N, M = (int(x) for x in raw_input().split())
        grid = []
        for i in range(N):
            grid.append([int(x) for x in raw_input().split()])

        if all(mowable(grid, h, N, M) for h in range(1, 101)):
            answer = 'YES'
        else:
            answer = 'NO'

        print "Case #%d: %s" % (testcase, answer)


def mowable(original_grid, h, N, M):
    grid = [[1 for j in range(M)] for i in range(N)]
    for i in range(N):
        if not any(original_grid[i][j] > h for j in range(M)):
            for j in range(M):
                grid[i][j] = 0
    for j in range(M):
        if not any(original_grid[i][j] > h for i in range(N)):
            for i in range(N):
                grid[i][j] = 0
    if any(original_grid[i][j] <= h and grid[i][j] == 1 for i in range(N) for j in range(M)):
        return False
    return True


main()
