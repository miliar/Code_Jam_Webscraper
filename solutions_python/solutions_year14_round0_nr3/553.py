#!/usr/local/bin/python
import itertools
import sys, getopt
from collections import deque

IMPOSSIBLE = "Impossible"

def neighbors(x, y, X, Y):
    return [(x2, y2) for x2 in range(x-1, x+2) if x2 >= 0 and x2 < X for y2 in range(y-1, y+2) if y2 >= 0 and y2 < Y and -1 < x <= X and -1 < y <= Y and (x != x2 or y != y2)]

def calculate_value(c, board, widht, height):
    ret = 0
    for n in neighbors(c[0], c[1], widht, height):
        if board.get(n, '.') == '*':
            ret += 1
    return ret

def generate_cell(r, c):
    return list(itertools.product(range(r), range(c)))

def generate_mine_distributions(cells, m):
    return itertools.combinations(cells, m)

def initialize_board(dist, c):
    ret = {}
    ret[c] = 'c'
    for mine in dist:
        ret[mine] = '*'
    return ret

def run_case(widht, height, cells, dist, c):
    board = initialize_board(dist, c)
    #cells_queue = deque(neighbors(c[0], c[1], widht, height))
    expanded = []
    cells_queue = deque([c])
    while len(cells_queue):
        cell = cells_queue.popleft()
        if not cell in expanded:
            expanded.append(cell)            
            val = calculate_value(cell, board, widht, height)
            board[cell] = val
            if val == 0:
                cells_queue.extend(neighbors(cell[0], cell[1], widht, height))
    if len(board) == widht*height:
        return True

def free_cells(cells, dist):
    return list(set(cells).difference(set(dist)))

def print_distribution(rows, columns, cells, dist, c):
    row = []
    for idx, cell in enumerate(cells):
        if cell in dist:
            v = '*'
        elif cell == c:
            v = 'c'
        else:
            v = '.'
        row.append(v)
        if (idx + 1) % columns == 0:
            print "".join(row)
            row = [] 


def resolve_test_case(r, c, m):
    if m >= r*c:
        print IMPOSSIBLE
        return

    cells = generate_cell(r, c)
    for d in generate_mine_distributions(cells, m):
        for f in free_cells(cells, d):
            if run_case(r, c, cells, d, f):
                print_distribution(r, c, cells, d, f)
                return
    print IMPOSSIBLE

if __name__ == "__main__":
    input_file = sys.argv[1]
    for idx, l in enumerate(open(input_file).readlines()[1:]):
        print "Case #{}:".format(idx + 1)
        r, c, m = l.split(' ')
        resolve_test_case(int(r), int(c), int(m))
    #resolve_test_case(3, 1, 1)
    #resolve_test_case(2, 2, 1)
    #resolve_test_case(4, 7, 3)
    #resolve_test_case(10, 10, 82)
