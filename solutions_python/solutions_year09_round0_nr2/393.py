import re


from numpy import *
from itertools import count

from helper_functions import *

def print_array(result):
    string = []
    offset = ord('a')-1
    for row in result:
        string.append('\n')
        string.append(' '.join(chr(i+offset) for i in row))
    return ''.join(string)
            
    print repr(result)

def solve_problem(input, output):
    N = getnum(input)
    for n in xrange(N):
        H, W = getnums(input)
        grid = empty((H,W), dtype=int)
        for h in xrange(H):
            grid[h, :] = getnums(input)
        result = solve_case(grid)
        answer(print_array(result), output)
    
def solve_case(heights):
    result = zeros_like(heights)
    fill = 1
    for coords, height in ndenumerate(heights):
        if result[coords] == 0:
            bottom = find_bottom(heights, coords)
            flood_from(heights, result, bottom, fill)
            fill += 1
    return result


def flood_from(heights, result, bottom, fill):
    q = [bottom]
    origin = array((0,0))
    edge = array(heights.shape)
    while q:
        coords = q.pop(0)
        assert result[coords] == 0
        result[coords] = fill
        for delta in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            neighbour = add(coords, delta)
            if any(neighbour<origin) or any(neighbour>=edge):
                pass
            else:
                if lowest_neighbour(heights, neighbour) == coords:
                    q.append(neighbour)

def find_bottom(heights, coords):
    direction = downhill_direction(heights, coords)
    while direction != (0, 0):
        direction = downhill_direction(heights, coords)
        coords = add(coords, direction)
    return coords

def lowest_neighbour(heights, coords):
    I, J = coords
    i, j = downhill_direction(heights, coords)
    return I+i, J+j
    
def downhill_direction(heights, coords):
    origin = array((0,0))
    edge = array(heights.shape)
    I, J = coords
    # null, noth, west, east, south
    min_height = heights[I, J]
    downhill = (0, 0)
    for i, j in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        neighbour = I+i, J+j
        if all(origin<=neighbour) and all(neighbour<edge):
            height = heights[neighbour]
            if  height < min_height:
                downhill = i, j
                min_height = height
    return downhill

def add(coords, direction):
    I, J = coords
    i, j = direction
    return I+i, J+j

if __name__ == "__main__":
    test_input = """
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8
    """
    test_output = """
Case #1:
a b b
a a b
a a a
Case #2:
a a a a a a a a a b
Case #3:
a a a
b b b
Case #4:
a a a a a
a a b b a
a b b b a
a b b b a
a a a a a
Case #5:
a b c d e f g h i j k l m
n o p q r s t u v w x y z
    """
    
    do_test(solve_problem, test_input, test_output)
    
    do_real(solve_problem)