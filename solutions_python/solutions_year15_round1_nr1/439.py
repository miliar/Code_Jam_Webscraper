f = open('A-large.in', 'r')

import itertools

output = ""

amountCases = int(f.readline())

def runCase():

    n = int(f.readline())

 
    data = [int(a) for a in f.readline().split()]
    
    difs = [ data[i] - data[i+1] for i in range( len(data) - 1) ]

    max_dif = max(difs)

    solution1, solution2 = 0,0

    for i in range( len(data) ):

        if i< len(data) -1:
            solution1 += max(0,difs[i])

            solution2 += min( max_dif, data[i] )

    return str(solution1) + " " + str(solution2)

        

            

            
for caseNumber in range(amountCases):

    print( "Case #" + str(caseNumber+1) + ": " + str( runCase() ) )


        

