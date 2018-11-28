import sys
from pprint import pprint

class Lawn(object):
    def __init__(self, pattern):
        self.pattern = pattern
        self.N = len(pattern)
        self.Ns = range(self.N)
        self.M = len(pattern[0])
        self.Ms = range(self.M)
        self.field = []
        for i in self.Ns:
            self.field.append([])
            for j in self.Ms:
                self.field[i].append(100)
        self.heigth = 100
    def is_solvable(self):
        if self.field == self.pattern:
            return 'YES'
        if not self.Ns and not self.Ms:
            return 'NO'
        self.improve()
        return self.is_solvable()
    def improve(self):
        #print self.heigth
        self.clean_heigth()
        self.heigth -= 1
        #pprint(self.field)
    def clean_heigth(self):
        ns = []
        ms = []
        for i, line in enumerate(self.pattern):
            for j, heigth in enumerate(line):
                if heigth == self.heigth:
                    #print i, j
                    ns.append(i)
                    ms.append(j)
                    if i not in self.Ns and j not in self.Ms:
                        self.Ns = []
                        self.Ms = []
                    else:
                        self.field[i][j] = heigth
        for n in set(ns):
            if n in self.Ns:
                self.Ns.pop(self.Ns.index(n))
        for m in set(ms):
            if m in self.Ms:
                self.Ms.pop(self.Ms.index(m))

def get_lawn(infile):
    [n, m] = [int(number) for number in infile.readline().split()]
    pattern = []
    for i in range(n):
        pattern.append([int(number) for number in infile.readline().split()])
    return Lawn(pattern)

filename = sys.argv[1]
with open(filename)as infile:
    with open('.'.join([filename.split('.')[0], 'out']), 'w') as outfile:
        cases = int(infile.readline())
        for case in range(cases):
            lawn = get_lawn(infile)
            solution = "Case #%d: %s\n" % (case + 1, lawn.is_solvable())
            outfile.write(solution)
