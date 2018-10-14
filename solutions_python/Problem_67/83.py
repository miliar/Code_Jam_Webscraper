import sys

def show_squares(squares):
    grid = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
           ]
    print squares
    for (x, y) in squares:
        grid[y][x] = 1
    print
    for line in grid:
        print line

def generations(squares):
    gens = 0
    #show_squares(squares)
    while len(squares):
        #print len(squares)
        next = set()
        # Survivors
        for s in squares:
            x, y = s
            if (x-1, y) in squares or (x, y-1) in squares:
                next.add(s)
        # New
        for north in squares:
            nx, ny = north
            if (nx-1, ny+1) in squares:
                next.add((nx, ny+1))
        squares = next
        #show_squares(squares)
        gens += 1
    return gens

def do_one_test_case(file):
    R = int(file.readline())
    rects = [[int(n) for n in file.readline().split()] for _ in xrange(R)]

    grid_dict = set((x, y)
                    for x1, y1, x2, y2 in rects
                    for x in xrange(x1, x2+1)
                    for y in xrange(y1, y2+1))
    #print grid_dict

    return generations(grid_dict)

def main(argv):
    f = open(argv[1], 'r')
    cases = int(f.readline())
    output_list = []
    for i in xrange(cases):
        output_list.append('Case #%d: %s\n' % (i+1, do_one_test_case(f)))
    f.close()
    if len(argv) > 2:
        expected_f = open(argv[2], 'r')
        expected_list = expected_f.readlines()
        expected_list = expected_list[0:-1]
        if (output_list == expected_list):
            print 'Everything matched!'
        else:
            print 'Actual: %s' % output_list
            print 'Expected: %s' % expected_list
    else:
        print ''.join(output_list)

def test():
    print 'Usage: scriptname.py infile [outfile]'
    print 'I\'ll run the doctests instead!'
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        test()
    else:
        main(sys.argv)
