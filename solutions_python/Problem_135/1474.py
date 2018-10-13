'''
Created on Apr 11, 2014

@author: Sean Groathouse
'''

fin = open('A-small.in', 'r')
finput = fin.readlines()
fin.close()

it = iter(finput)

numbCases = int(it.next())

output = ""

for case in xrange(numbCases):    
    firstAnswer = int(it.next())
    firstGrid = []
    for _i in xrange(4):
        row = [int(j) for j in (it.next()).split()]
        firstGrid.append(row)
    
    secondAnswer = int(it.next())
    secondGrid = []
    for _i in xrange(4):
        row = [int(j) for j in (it.next()).split()]
        secondGrid.append(row)
        
    optionsOne = firstGrid[firstAnswer-1] # one-indexed
    optionsTwo = secondGrid[secondAnswer-1] # one-indexed
    
    possibilities = [value for value in optionsOne if value in optionsTwo]
    
    if (len(possibilities) == 1):
        output += "Case #%d: %d\n" % (case+1, possibilities[0])
    elif (len(possibilities) == 0):
        output += "Case #%d: Volunteer cheated!\n" % (case+1)
    else:
        output += "Case #%d: Bad magician!\n" % (case+1)
    
fout = open('small.txt', 'w')
fout.write(output)
fout.close