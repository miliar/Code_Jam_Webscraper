#6:20pm
test_case = \
'''\
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
'''

test_solution = \
'''\
Case #1: YES
Case #2: NO
Case #3: YES
'''

from collections import Counter, defaultdict
from operator import itemgetter

class Solver:

    def __init__(self, reader):
        self.reader = reader
        
    def solve(self):
        n, m = self.reader.get_list()
        pattern = self.reader.get_matrix(n, m)
        done = set()
        for i in range(n):
            for j in range(m):
                if (i,j) in done:
                    continue
                h = pattern[(i,j)]
                if all(pattern[(i,k)]<=h for k in range(m)):
                    # row ok
                    done |= {(i,k) for k in range(m) if pattern[(i,k)]==h}
                    continue
                if all(pattern[(k,j)]<=h for k in range(n)):
                    # col ok
                    done |= {(k,j) for k in range(n) if pattern[(k,j)]==h}
                    continue
                return 'NO'
        return 'YES'