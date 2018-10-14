'''
Problem D: Ominous Omino
'''

def readInput(filename, parser):
    with open(filename, 'r') as infile:
        data = infile.readlines()
        return parser(data)

def writeOutput(filename, solver, data):
    with open(filename, 'w') as outfile:
        for i, case in enumerate(data):
            outfile.write("Case #{0}: ".format(i+1) + str(solver(case)) + '\n')
            
            
def ominoParser(data):
    numcases = 0
    cases = []
    for i, line in enumerate(data):
        if i == 0:
            numcases = int(line)
        else:
            sline = line.split(' ')
            cases.append(Case(int(sline[0]), int(sline[1]), int(sline[2])))
    return cases

def Solve(case):
    # First check obvious contraints:
    # - X cannot be large than 6 or Richard can pick a shape with a hole in it which cannot be filled
    # - X much be smaller than at least one dimension of the grid of Richard can choose the longest X-omino and win
    # - R*C must be a multiple of X or it cannot be tiled
    if (case.X > 6) or ((case.X > case.C) and (case.X > case.R)) or ((case.R * case.C) % case.X != 0):
        return "RICHARD"
    else:
        #For X=1 and X=2, only one X-omino exists, and if the above conditions are met, they will tile.
        if (case.X == 1) or (case.X == 2):
            return "GABRIEL"
        elif (case.X == 3):
            if case.R == 1 or case.C == 1:
                return "RICHARD"
            else:
                return "GABRIEL"
        elif (case.X == 4):
            if case.R == 1 or case.C == 1:
                return "RICHARD"
            elif case.R == 2 or case.C == 2:
                return "RICHARD"
            elif case.R == 3 or case.C == 3:
                return "GABRIEL"
            elif case.R == 4 or case.C == 4:
                return "GABRIEL"
    
    
            
class Case(object):

    X = 0
    R = 0
    C = 0

    def __init__(self, x, r, c):
        self.X = x
        self.R = r
        self.C = c
            
            
if __name__ == "__main__":
    filename = 'D-small-attempt0.in'
    outfile = 'ominoSmall.out'

    data = readInput(filename, ominoParser)
    writeOutput(outfile, Solve, data)