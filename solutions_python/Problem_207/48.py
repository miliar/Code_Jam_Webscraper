__author__ = 'sware'

import sys, collections, heapq

inputfile = file(sys.argv[1])
outputfile = file(sys.argv[2], 'w')

cantbe = {}
cantbe['R'] = set(['R', 'O', 'V'])
cantbe['Y'] = set(['Y', 'O', 'G'])
cantbe['B'] = set(['B', 'G', 'V'])
cantbe['O'] = cantbe['R'].union(cantbe['Y'])
cantbe['G'] = cantbe['Y'].union(cantbe['B'])
cantbe['V'] = cantbe['R'].union(cantbe['B'])

for case in xrange(int(inputfile.readline())):
    N, R, O, Y, G, B, V = map(int, inputfile.readline().split())
    numtype = [[R, 'R'], [O, 'O'], [Y, 'Y'], [G, 'G'], [B, 'B'], [V, 'V']]
    numtype.sort()
    numtype.reverse()
    if numtype[0][0] > numtype[1][0] + numtype[2][0]:
        outputfile.write('Case #{}: {}\n'.format(case+1, 'IMPOSSIBLE'))
        continue
    solution = []
    #print numtype
    #print 'case'
    while len(solution) != N:
        #print numtype
        if numtype[0][0] > numtype[1][0]:
            solution.append(numtype[0][1])
            solution.append(numtype[1][1])
            numtype[0][0] -= 1
            numtype[1][0] -= 1
            if numtype[2][0] > numtype[1][0]:
                t = numtype[1]
                numtype[1] = numtype[2]
                numtype[2] = t
        elif numtype[1][0] > numtype[2][0]:
            solution.append(numtype[0][1])
            solution.append(numtype[1][1])
            numtype[0][0] -= 1
            numtype[1][0] -= 1
        else:
            solution.append(numtype[0][1])
            solution.append(numtype[1][1])
            solution.append(numtype[2][1])
            numtype[0][0] -= 1
            numtype[1][0] -= 1
            numtype[2][0] -= 1
    outputfile.write('Case #{}: {}\n'.format(case+1, ''.join(solution)))
outputfile.close()