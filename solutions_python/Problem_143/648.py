from __future__ import division


FILE_NAME = 'B-small-attempt0.in'

numCases = 0
testCases = []
with open(FILE_NAME,'r') as file:
    numCases = int(file.readline())
    for case in xrange(numCases):
        testCases.append([int(x) for x in file.readline().split()])
           

def lottery(old_max,new_max,played_max):
    total = 0
    for old in xrange(old_max):
        for new in xrange(new_max):
            if old & new < played_max:
                total += 1
    return total
        

    
    
caseNum = 1
with open('results.txt','w') as file:
    for test in testCases:
        file.write('Case #{}: {}\n'.format(caseNum,lottery(test[0],test[1],test[2])))
        caseNum += 1
    

