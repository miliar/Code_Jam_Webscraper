import math

def process_case(case):
    x, r, c = map(int, case.split())

    # (7+)-onimos can have a hole in the middle. 
    if x >= 7:
        return False
    
    cells_in_grid = r * c

    # number of cells in grid must be evenly
    # divisible by number of cells in omino
    if (cells_in_grid % x != 0):
        return False

    # is x larger than r and c? if so the straight omino
    # cannot be placed.
    if x > r and x > c:
        return False

    # is there an x-omino permutation with both sides larger than
    # either r or c?
    smallest_side = r if r < c else c
    if smallest_side < (x - 1):
        return False

    return True

with open('omino_in.txt', 'r') as f, open('omino_out.txt', 'w') as g:
    num_tests = int(f.readline().strip())
    for i in range(num_tests):
        solution_exists = process_case(f.readline())
        winner = "GABRIEL" if solution_exists else "RICHARD"
        g.write('Case #%s: %s\n' % (i+1, winner))
