import os
import sys
from collections import defaultdict
sys.setrecursionlimit(1999999999)
problem_id = 'A'

sys.setrecursionlimit(10**9)
input_path = '%s.in' % problem_id
output_path = '%s.out' % problem_id


def read_line():
    line = ''
    while len(line) == 0:
        line = input_file.readline().strip()
    return line


def write_line(line):
    print line
    return output_file.write(line + os.linesep)

def solve():
    r, c = map(int, read_line().split(' '))
    grid = [read_line() for i in range(r)]
    x = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] != '.':
                left = False
                right = False
                up = False
                down = False
                for k in range(i+1, r):
                    if grid[k][j] != '.':
                        down = True
                        break
                for k in range(i-1, -1, -1):
                    if grid[k][j] != '.':
                        up = True
                        break
                for k in range(j-1, -1, -1):
                    if grid[i][k] != '.':
                        left = True
                        break
                for k in range(j+1, c):
                    if grid[i][k] != '.':
                        right = True
                        break
                if not left and not right and not up and not down:
                    return 'IMPOSSIBLE'
                cc = grid[i][j]
                if not (cc == '^' and up or cc == 'v' and down or cc =='<' and left or cc == '>' and right):
                    x += 1
    return '%d' % x




input_file = open(input_path, "r")
output_file = open(output_path, "w+")
T = int(read_line())
for case_id in xrange(1, T + 1):
    write_line("Case #%d: %s" % (case_id, solve()))
input_file.close()
output_file.close()