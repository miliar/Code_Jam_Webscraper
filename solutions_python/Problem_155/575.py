'''
Standing Ovation Solver
'''
def readInput(filename, parser):
    with open(filename, 'r') as infile:
        data = infile.readlines()
        return parser(data)
    
def writeOutput(filename, solver, data):
    with open(filename, 'w') as outfile:
        for i, case in enumerate(data):
            outfile.write("Case #{0}: ".format(i+1) + str(solver(case)) + '\n')
    
def ovationParser(data):
    ncases = 0
    cases = []
    
    for i, line in enumerate(data):
        if i == 0:
            ncases = int(line)
        else:
            sline = line.split(' ')
            Smax = sline[0]
            pList = sline[1].replace('\n', '')
            cases.append(Case(Smax, pList))
            
    return (ncases, cases)

def Solve(case):
    ntotal = 0
    nreq = 0
    slevel = 0
    for i in case.plist:
        ntotal += int(i)
        if slevel < case.smax:
            if (ntotal < slevel+1):
                nreq += (slevel+1) - ntotal
                ntotal += (slevel+1) - ntotal
            slevel += 1
    return nreq
            
class Case(object):
    smax = 0
    plist = []
    def __init__(self, Smax, pList):
        self.smax = Smax
        self.plist = pList
        

if __name__ == "__main__":
    filename = 'A-large.in'
    outfile = 'ovationresultslarge.out'
    
    data = readInput(filename, ovationParser)
    writeOutput(outfile, Solve, data[1])