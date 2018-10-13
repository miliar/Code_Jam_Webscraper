problem = 'Magicka'
t = 's'
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
        line = get().split()
        C = int(line[0]) + 1
        self.c = line[1:C]
        self.c_dict = {}
        for c in self.c:
            self.c_dict[''.join(sorted([c[0],c[1]]))] = c[2]
        
        D = int(line[C]) + C + 1
        self.d = line[C+1:D]
        self.d_sets = {}
        for d in self.d:
            if d[0] not in self.d_sets:
                self.d_sets[d[0]] = set()
            self.d_sets[d[0]].add(d[1])
            if d[1] not in self.d_sets:
                self.d_sets[d[1]] = set()
            self.d_sets[d[1]].add(d[0])

        self.n = line[-1]
        print (self.c)
        print (self.d)
        print (self.n)
    
    def weight(self):
        # Return the value that determines the weight of the solution (for timing)
        return len(self.n)
    
    def solve(self):
        # Return the solution dictionary for this case
        self.result = [self.n[0]]
        self.used = set(self.result)
        for i in self.n[1:]:
            if len(self.result) > 0:
                if ''.join(sorted([self.result[-1], i])) in self.c_dict:
                    c = self.result.pop(-1)
                    self.result += [self.c_dict[''.join(sorted([c, i]))]]
                    self.used = set(self.result)
                    continue
                if i in self.d_sets:
                    if(self.d_sets[i] <= self.used):
                        self.result = []
                        self.used = set()
                        continue
            self.result += [i]
            self.used.add(i)
            
        return '[{0}]'.format(', '.join([self.result[i] for i in range(len(self.result))]))
    
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
        