FILE_NAME = 'B-large.txt'


numCases = 0
testCases = []
with open(FILE_NAME,'r') as file:
    numCases = int(file.readline())
    for e in xrange(numCases):
        a = int(file.readline().split(' ')[0])
        testCases.append([])

        for row in xrange(a):
            testCases[e].append([int(x) for x in file.readline().split(' ')])



def possible(lawn):

    #Get Max Height for Rows/Columns
    rowMax = [max(row) for row in lawn]
    columnMax = []
    for column in xrange(len(lawn[0])):
        columnMax.append(max([row[column] for row in lawn]))

                
    #Check inner squares against max height/row
    for row in xrange(0,len(lawn)):
        for column in xrange(0,len(lawn[0])):
            if lawn[row][column] != rowMax[row] and \
               lawn[row][column] != columnMax[column]:
                return 'NO'
    else:
        return 'YES'

    
    

caseNum = 1
with open('results.txt','w') as file:
    for test in testCases:
        file.write('Case #{}: {}\n'.format(caseNum,possible(test)))
        caseNum += 1
    
