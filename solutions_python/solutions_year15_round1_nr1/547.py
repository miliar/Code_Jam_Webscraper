'''
Problem C: Dijkstra
'''

import numpy as np

def readInput(filename, parser):
    with open(filename, 'r') as infile:
        data = infile.readlines()
        return parser(data)

def writeOutput(filename, solver, data):
    with open(filename, 'w') as outfile:
        for i, case in enumerate(data):
            outfile.write("Case #{0}: ".format(i+1) + str(solver(case)) + '\n')

def Parser(data):
    cases = []
    for i, line in enumerate(data):
        if i > 0:
            if (i%2 == 0):
                cases.append(Case([int(x) for x in line.split(' ')]))
                
    return cases
            

def Solve(case):
    min1 = 0
    min2 = 0
    largestdif = -min(np.diff(case.m))
    for i in range(len(case.m)-1):
        dif = (case.m[i] - case.m[i+1])
        if dif > 0:
            min1 += dif
        min2 += min(largestdif, case.m[i])
            
    return str(min1) + ' ' + str(min2)
            

        

class Case(object):

    m = []
    
    def __init__(self, array):
        self.m = array
        
    def GenerateFullstring(self):
        pass
        

if __name__ == "__main__":
    filename = 'A-large.in'
    outfile = 'A-large.out'

    data = readInput(filename, Parser)
    writeOutput(outfile, Solve, data)