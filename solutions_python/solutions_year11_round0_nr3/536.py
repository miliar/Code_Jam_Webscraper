problem = 'CandySplitting'
t = 'l'
debug = True

middle = {'t': 'ex', 's': 'small', 'l': 'large'}[t]

input_file = open('{problem}-{middle}.in'.format(**globals()))
output_file = open('{problem}-{middle}.out'.format(**globals()), 'w')

import decimal

# Helper functions
def split_to_ints(s):
    return [i for i in map(int, s.split())]

def list_to_index_tuple(l, base=0):
    return [(i + base, l[i]) for i in range(len(l))]

class Solution:
    format = '{0}' # The format string for solutions
    
    def __init__(self, get):
        # Read in the entire solution
        get() # Discard the number of candies
        self.C = split_to_ints(get())
    
    def weight(self):
        # Return the value that determines the weight of the solution (for timing)
        return len(self.C)
    
    def solve(self):
        # Return the solution dictionary for this case
        x = self.C[0]
        for c in self.C[1:]:
            x = x ^ c
        if x != 0: return 'NO'
        return sum([i for i in sorted(self.C)][1:])
    
if debug: from time import clock
    
if __name__ == '__main__':
    get = input_file.readline
    n = int(get())
    durations = []
    for i in range(n):
        s = Solution(get)
        if debug:
            print ('Case {} started'.format(i))
            start = clock()
        o = s.format.format(s.solve())
        if debug:
            duration = clock() - start
            durations += [(duration, s.weight())]
            print ('Case {} solved in {}'.format(i, durations[-1][0]))
            print ('Weight {}, so: {}'.format(durations[-1][1], durations[-1][0] / durations[-1][1]))
        output_file.write('Case #{}: {}\n'.format(i+1, o))
    if debug:
        mean = sum(x[0] for x in durations) / len(durations)
        maxdiff = 0
        for x in durations:
            maxdiff = max(maxdiff, abs(mean-x[0]))
        if maxdiff/mean < .25: print('O(1)')
        else: print('> O(1)')
        mean = sum(x[0]/x[1] for x in durations) / len(durations)
        maxdiff = 0
        for x in durations:
            maxdiff = max(maxdiff, abs(mean-(x[0]/x[1])))
        if maxdiff/mean < .25: print('O(N)')
        else: print('> O(N)')
        