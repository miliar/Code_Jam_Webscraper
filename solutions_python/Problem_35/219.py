import os.path
import itertools
import string
#import arrays

altitude_invalid = 99999
output_invalid = ' '

class _Matrix(object):
    def __init__(self, values, rows, cols, default):
        self.rows = rows
        self.columns = cols
        self.array = values
        self.default = default
    def get(self, r, c):
        if r not in self.array or c not in self.array[r]: return self.default
        return self.array[r][c]
    def set(self, r, c, value):
        self.array[r][c] = value
    def __iter__(self):
        return iter(self.array)
    def for_each(self, callback_func):
        for r in xrange(self.rows):
            for c in xrange(self.columns):
                callback_func(r, c, self.get(r,c))
    def __repr__(self):
        return '\n'.join(' '.join(str(self.get(r, c)) for c in xrange(self.columns)) for r in xrange(self.rows))

def Matrix(values, rows, cols, default):
    d = dict()
    for r, row in itertools.izip(itertools.count(0), values):
        rowdict = dict()
        d[r] = rowdict
        for c, value in itertools.izip(itertools.count(0), row):
            rowdict[c] = value
    return _Matrix(d, rows, cols, default)

def Matrix2(rows, cols, initial):
    d = dict()
    for r in xrange(rows):
        rowdict = dict()
        d[r] = rowdict
        for c in xrange(cols):
            rowdict[c] = initial
    return _Matrix(d, rows, cols, initial)

SINK=0
NORTH=1
WEST=2
EAST=3
SOUTH=4

def get_dir(*args): #north, west, east, south, current):
    #print args
    return min(itertools.izip(args, [NORTH,WEST,EAST,SOUTH,SINK]))[1]

def test_get_dirs():
    assert(get_dir(6,5,6,5,9) == 2)
    assert(get_dir(99999,6,99999,6,3) == 0)
    assert(get_dir(99999,99999,6,5,9) == 4)
    assert(get_dir(9,99999,9,99999,9) == 0)
    assert(get_dir(9,9,4,4,4) == 0)

class Problem(object):
    def __init__(self, altitudes):
        self.altitudes = altitudes
        self.out_matrix = None
        self.basins = list(string.lowercase)
    def _get_next_basin(self):
        return self.basins.pop(0)
    def run(self):
        #print self.altitudes
        self.out_matrix = Matrix2(self.altitudes.rows, self.altitudes.columns,
                output_invalid)
        for r in xrange(self.altitudes.rows):
            for c in xrange(self.altitudes.columns):
                self._recurse(r, c)
        return self.out_matrix
    def _recurse(self, r, c):
        v = self.out_matrix.get(r, c)
        if v != output_invalid:
            return v
        current = self.altitudes.get(r, c)
        north = self.altitudes.get(r-1, c)
        west  = self.altitudes.get(r, c-1)
        east  = self.altitudes.get(r, c+1)
        south = self.altitudes.get(r+1, c)
        # pick direction
        direction = get_dir(north, west, east, south, current)
        #print r, c, direction
        if direction == SINK:
            v = self._get_next_basin()
        elif direction == NORTH:
            v = self._recurse(r-1, c)
        elif direction == WEST:
            v = self._recurse(r, c-1)
        elif direction == EAST:
            v = self._recurse(r, c+1)
        elif direction == SOUTH:
            v = self._recurse(r+1, c)
        self.out_matrix.set(r, c, v)
        return v
        
def test_basic_problem():
    p = Problem(Matrix([[9,6,3],[5,9,6],[3,5,9]], 3,3, altitude_invalid))
    assert (str(p.run()) == 'a b b\na a b\na a a')

def run(filename, outfile):
    input = open(filename, 'r')
    lines = input.readlines()
    input.close()
    out = open(outfile, 'w')
    first = lines.pop(0).strip()
    tee = int(first)
    for i in xrange(tee):
        sizes = lines.pop(0).split()
        rows = int(sizes[0])
        cols = int(sizes[1])
        rowlist = []
        for j in xrange(rows):
            rowlist.append(map(int, lines.pop(0).split()))
        p = Problem(Matrix(rowlist, rows, cols, altitude_invalid))
        out.write('Case #%d:\n%s\n' % (i+1, p.run()))
        out.flush()
    out.close()

    
if __name__ == '__main__':
    import sys
    run(sys.argv[1], sys.argv[2])

