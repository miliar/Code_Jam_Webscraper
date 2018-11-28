import sys
import re

def make_basin_string(basins):
    def make_line(ns):
        return ' '.join(chr(ord('a') + n) for n in ns)
    return '\n' + '\n'.join(make_line(row) for row in basins)

class Flower(object):
    def __init__(self, heights):
        self.h = len(heights)
        self.w = len(heights[0])
        self.heights = heights
	self.pos_to_basin = {}
	self.basin_count = 0
    def get_basin(self, y, x):
        p = (y, x)
	#sys.stderr.write('%s\n' % str(p))
	if p not in self.pos_to_basin:
            height_at_point = self.heights[y][x]
	    candidates = []
	    if (y > 0) and (self.heights[y-1][x] < height_at_point):
		candidates.append((y-1, x, 0))
	    if (x > 0) and (self.heights[y][x-1] < height_at_point):
                candidates.append((y, x-1, 1))
	    if (x+1 < self.w) and (self.heights[y][x+1] < height_at_point):
                candidates.append((y, x+1, 2))
	    if (y+1 < self.h) and (self.heights[y+1][x] < height_at_point):
                candidates.append((y+1, x, 3))
	    #sys.stderr.write('Len: %d\n' % len(candidates))
            if len(candidates) == 0:
                self.pos_to_basin[p] = self.basin_count
		self.basin_count += 1
            else:
                heights = [(self.heights[y][x], p, (y, x)) for (y, x, p) in iter(candidates)]
	        #sys.stderr.write('Heights: %s\n' % str(heights))
		heights.sort()
                _, _, (toy, tox) = heights[0]
                self.pos_to_basin[p] = self.get_basin(toy, tox)

        return self.pos_to_basin[p]

def get_basin_string(heights):
    h = len(heights)
    w = len(heights[0])
    flower = Flower(heights)
    get_basin = flower.get_basin
    basins = ((get_basin(y, x) for x in xrange(w)) for y in xrange(h))
    return make_basin_string(basins)

def do_one_test_case(file):
    h, w = (int(n) for n in file.readline().strip().split())
    heights = []
    for _ in xrange(h):
        heights.append(list(int(n) for n in file.readline().strip().split()))
    return get_basin_string(heights)

def main(argv):
    f = open(argv[1], 'r')
    cases = int(f.readline().strip())
    sys.stderr.write('Cases: %d\n' % cases)
    output_list = []
    for i in xrange(cases):
        output_list.append('Case #%d:%s\n' % (i+1, do_one_test_case(f)))
        sys.stderr.write('%d of %d done\n' % (i+1, cases))
    f.close()
    if len(argv) > 2:
        expected_f = open(argv[2], 'r')
        expected_list = expected_f.readlines()
        expected_list = [line.strip()+'\n' for line in expected_list[0:-1]]
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
