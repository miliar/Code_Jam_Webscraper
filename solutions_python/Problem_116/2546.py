from itertools import permutations
import sys

status = {'x': 'X won', 'o': 'O won', 'draw': 'Draw', 'not_over': 'Game has not completed'}

# Returns list of all possible (10) lines 
def get_lines(grid):
    lines = []

    # each row
    for line in grid:
        lines.append(line)

    # each column
    for x in xrange(len(grid)):
        line = "%s%s%s%s" % (grid[0][x], grid[1][x], grid[2][x], grid[3][x])
        lines.append(line)
    
    # diagonal from top left to bottom right
    line = "%s%s%s%s" % (grid[0][0], grid[1][1], grid[2][2], grid[3][3])
    lines.append(line)

    # diagonal from top right to bottom left
    line = "%s%s%s%s" % (grid[0][3], grid[1][2], grid[2][1], grid[3][0])
    lines.append(line)

    return lines

# Returns whether grid is full or not
def grid_is_full(grid):
    for line in grid:
        if '.' in line:
            return False
    return True

# List of possible permutations of a winning row
x_perm = [''.join(x) for x in permutations('XXXT')]
x_perm.append('XXXX')
o_perm = [''.join(x) for x in permutations('OOOT')]
o_perm.append('OOOO')

def check_line(line):
    if line in x_perm:
        return 'x'
    elif line in o_perm:
        return 'o'
    else:
        return None

# Returns game status
def game_status(grid):
    lines = get_lines(grid)
    for line in lines:
        result = check_line(line)
        if result == 'x': 
            return status['x']
        elif result == 'o':
            return status['o']
    if grid_is_full(grid):
        return status['draw']
    return status['not_over']

N = int(raw_input())
for x in xrange(N):
    lines = []
    for y in xrange(4):
        lines.append(raw_input())
    raw_input()
    print "Case #%d: %s" % ((x+1), game_status(lines))

