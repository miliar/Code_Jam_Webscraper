import sys
import numpy as np

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    filename = argv[0] if argv else 'test.in'

    with open(filename) as f:
        num_cases = int(f.readline())
        for case_no in xrange(1, num_cases+1):
            grid = []
            for i in xrange(4):
                grid.append(list(f.readline().strip()))
            grid = np.array(grid)
            state = get_state(grid)
            print 'Case #{}:'.format(case_no),
            if state == 'X':
                print "X won"
            elif state == 'O':
                print "O won"
            elif state == '.':
                print "Game has not completed"
            else:
                print "Draw"
            
            f.readline()

def get_state(grid):
    full = True
    states = {
            (0, 1) : [(i, 0) for i in xrange(4)],
            (1, 0) : [(0, i) for i in xrange(4)],
            (+1, +1) : [(0, 0)],
            (+1, -1) : [(0, 3)],
            }
    for delta, starts in states.iteritems():
        for s in starts:
            result = check_inds(grid, s, delta)
            if result == '.':
                full = False
            elif result != '!':
                return result
    if full:
        return '!'
    else:
        return '.'

def check_inds(grid, start, delta):
    pos = start
    type = 'T'
    for i in xrange(4):
        if grid[pos] == '.':
            return '.'
        if grid[pos] != 'T':
            if type != 'T' and type != grid[pos]:
                return '!'
            type = grid[pos]

        pos = tuple(np.array(pos) + delta)
    return type

if __name__ == '__main__':
    main()
