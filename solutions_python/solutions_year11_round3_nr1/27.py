import math
from collections import defaultdict

class TestCase(object):
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def from_input(cls, input):
        data = defaultdict(bool)
        for i, row in enumerate(input):
            for j, c in enumerate(row):
                data[(i,j)] = c
        data['rows'] = len(input)
        data['cols'] = len(input[0])
        return cls(data)
    
    def solve(self):
        data = self.data
        for i in xrange(data['rows']):
            for j in xrange(data['cols']):
                val = data[(i, j)]
                if val == '#':
                    vals = data[(i,j+1)], data[(i+1,j)], data[(i+1,j+1)]
                    if vals != ('#', '#', '#'):
                        return "Impossible"
                    data[(i,j)] = '/'
                    data[(i,j+1)] = '\\'
                    data[(i+1,j)] = '\\'
                    data[(i+1,j+1)] = '/'
        for i in xrange(data['rows']):
            for j in xrange(data['cols']):
                if val == '#':
                    return "Impossible"
        s = []
        for i in xrange(data['rows']):
            r = []
            for j in xrange(data['cols']):
                r.append(data[(i,j)])
            s.append("".join(r))
        return "\n".join(s)

f = open("inputs/tiles-large.in", "r")
test_cases = int(f.readline())

for i in range(test_cases):
    rows, columns = f.readline().split()
    test_case = TestCase.from_input([f.readline().strip() for j in range(int(rows))])
    print "Case #%d:\n%s" % (i+1, test_case.solve())
