'''
Problem C: Dijkstra
'''

quatdict = {'1': {'1': (1,'1'), 'i': (1,'i'),   'j': (1,'j'),  'k': (1, 'k')},
            'i': {'1': (1,'i'), 'i': (-1, '1'), 'j': (1,'k'),  'k': (-1,'j')},
            'j': {'1': (1,'j'), 'i': (-1,'k'),  'j': (-1,'1'), 'k': (1, 'i')},
            'k': {'1': (1,'k'), 'i': (1,'j'),  'j': (-1, 'i'), 'k': (-1, '1')}}

def readInput(filename, parser):
    with open(filename, 'r') as infile:
        data = infile.readlines()
        return parser(data)

def writeOutput(filename, solver, data):
    with open(filename, 'w') as outfile:
        for i, case in enumerate(data):
            outfile.write("Case #{0}: ".format(i+1) + str(solver(case)) + '\n')

def dijParser(data):
    numcases = 0
    cases = []
    for i, line in enumerate(data):
        if i == 0:
            numcases = i
        elif (i%2 == 1):
            sline = line.split(' ')
            cases.append(Case(data[i+1].replace('\n', ''), int(sline[1])))
    return cases

def Solve(case):
    fullstring = case.GenerateFullstring()
    curchar = '1'
    cursign = 1
    searchidx = 0
    searchchar = ['i', 'j', 'k']
    
    
    for char in fullstring:
        cursign *= quatdict[curchar][char][0]
        curchar = quatdict[curchar][char][1]
        if searchidx < 3 and curchar == searchchar[searchidx]:
            searchidx += 1
            curchar = '1'
    if searchidx >= 3 and curchar == '1' and cursign == 1:
        return "YES"
    else:
        return "NO"
        

class Case(object):

    bstring = ''
    rep = 0

    def __init__(self, bString, Rep):
        self.bstring = bString
        self.rep = Rep
        
    def GenerateFullstring(self):
        return self.bstring * self.rep
        

if __name__ == "__main__":
    filename = 'C-small-attempt0.in'
    outfile = 'dijkstrasmall.out'

    data = readInput(filename, dijParser)
    writeOutput(outfile, Solve, data)