import sys

class N_Finder(object):
    def __init__(self, name, n):
        self.name = name.lower()
        self.L = len(self.name)
        self.n = n
        self.indexes = []
    def solve(self):
        self.get_indexes()
        return self.count_ns()
    def get_indexes(self):
        for i, c in enumerate(self.name):
            if i+self.n > self.L:
                break
            #print self.name[i:i+self.n]
            if all(map(is_consonant, self.name[i:i+self.n])):
                self.indexes.append(i)
        #print self.indexes
    def count_ns(self):
        last_index = -1
        N = 0
        for start in self.indexes:
            end = start + self.n
            number = self.L - end + 1
            multiplier = start - last_index
            N += number * multiplier
            last_index = start
        return N

def is_consonant(char):
    return not char in 'aeiou'

def get_finder(infile):
    name, n = infile.readline().split()
    n = int(n)
    return N_Finder(name, n)

filename = sys.argv[1]
with open(filename)as infile:
    with open('.'.join([filename.split('.')[0], 'out']), 'w') as outfile:
        cases = int(infile.readline())
        for case in range(cases):
            finder = get_finder(infile)
            answer = finder.solve()
            solution = "Case #%d: %d\n" % (case + 1, answer)
            outfile.write(solution)
