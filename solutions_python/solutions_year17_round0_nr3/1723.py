# -*- coding: utf-8 -*-
import fractions
import math

def printResult(i,max,min,outfile):
    text = 'Case #' + str(i + 1) + ': ' + max + ' '+ min
    print(text)
    outfile.write(text + '\n')


fileName = 'C-small-2-attempt0'
with open(fileName+'.in', 'r') as infile, open(fileName + '_output.out', 'w') as outfile:
   
    T = int(infile.readline().split('\n')[0])
    
    for z in range(0,T):

        line = infile.readline().split('\n')[0].split(' ')
        N = int(line[0])
        K = int(line[1])

        tower = [[1],[N]]
        i = K
        while  i > 0 :
            M = max(tower[1])
            idx = tower[1].index(M)
            idxnum = tower[0][idx]
            steps = min(idxnum,i)

            if steps == idxnum :
                del tower[0][idx]
                del tower[1][idx]
            else :
                tower[0][idx] = tower[0][idx] - steps

            N1 = math.ceil((M-1)/2)
            if N1 in tower[1] :
                idx = tower[1].index(N1)
                tower[0][idx] = tower[0][idx] + steps
            else :
                tower[0].append(steps)
                tower[1].append(N1)

            N2 = math.floor((M-1)/2)

            if N2 in tower[1] :
                idx = tower[1].index(N2)
                tower[0][idx] = tower[0][idx] + steps
            else :
                tower[0].append(steps)
                tower[1].append(N2)

            i -= steps
            if i == 0 :
                maxdist = N1
                mindist = N2

        printResult(z, str(maxdist),str(mindist), outfile);



        
    
    
    
