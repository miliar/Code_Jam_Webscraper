import sys
import re
from itertools import *

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



def value_in(needle, needle_max, haystack, haystack_max, i_n, i_h):
    if i_n == needle_max:
        return True
    if i_h == haystack_max:
        return False
    i_h_next = haystack.find(needle[i_n], i_h, haystack_max)
    if i_h_next == -1:
        return False
    else:
        return value_in(needle, needle_max, haystack, haystack_max, i_n+1,
                i_h_next)

happies = dict()
for i in range(2, 11):
    happies[i] = set(['1'])

not_happy = dict()
for i in range(2, 11):
    not_happy[i] = set()

def new_base(i, base):
    r = ''
    while i > 0:
        r = str(i % base) + r
        i /= base
    return r

def get_square_sum(n, base):
    val = 0
    for digit in n:
        d = int(digit, base)
        val += d*d
    return new_base(val, base)

def is_happy(n, base, done=None):
    if done is None: done = tuple()
    #print n, base, done
    if n in happies[base]:
        return True
    if n in not_happy[base]:
        return False
    next = get_square_sum(n, base)
    if next in done:
        not_happy[base].add(n)
        return False
    elif next in happies[base]:
        happies[base].add(n)
        return True
    elif next in not_happy[base]:
        not_happy[base].add(n)
        return False
    elif is_happy(next, base, (n,) + done):
        happies[base].add(n)
        return True
    else:
        not_happy[base].add(n)
        return False
    
def problem(*args):
    for i in count(2):
        ok = True
        for base in args:
            if not is_happy(new_base(i, base), base):
                ok = False
                break
        if ok:
            return i


def put_output(out, number, count):
    out.write('Case #%d: %d\n' % (number, count))
    out.flush()

def run(infile, outfile):
    input = open(infile, 'r')
    lines = input.readlines()
    input.close()
    outfile = open(outfile, 'w')
    first = lines.pop(0).strip()
    num = int(first)
    for i in xrange(num):
        #print i
        p = [int(_i) for _i in lines.pop(0).strip().split()]
        #print p
        v = problem(*p)
        #print v
        put_output(outfile, i+1, v)
        outfile.flush()
    outfile.close()
if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
    #test_run()
    #pass

