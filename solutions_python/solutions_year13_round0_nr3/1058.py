#6:20pm
test_case = \
'''\
3
1 4
10 120
100 1000
'''

test_solution = \
'''\
Case #1: 2
Case #2: 0
Case #3: 2
'''

from collections import Counter, defaultdict
from operator import itemgetter
from math import sqrt

class Solver:

    def __init__(self, reader):
        self.reader = reader
        
    def is_fair(self, n):
        s = str(n)
        return s == s[::-1]
    
    def is_square(self, n):
        s = round(sqrt(n))
        return s * s == n and self.is_fair(s)
                
    def solve(self):
        a, b = self.reader.get_list()
        count = 0
        for n in range(a, b+1):
            if self.is_fair(n) and self.is_square(n):
                count+=1
        return count