FILE_NAME = 'D-large.in'

numCases = 0
testCases = []
with open(FILE_NAME,'r') as file:
    numCases = int(file.readline())
    for case in xrange(numCases):
        _ = file.readline()
        testCases.append([])
        testCases[case].append([float(x) for x in file.readline().split()])
        testCases[case].append([float(x) for x in file.readline().split()])

        
def findHigher(sortedlist,target):
    for index, value in enumerate(sortedlist):
        if value > target: return index

def war(a,b):
    a, b = a[:], b[:]
    a.sort()
    b.sort()
    a_wins = 0
    for x in xrange(len(a)):
        if a[-1] > b[-1]:
            a_wins += 1
            a.pop(-1)
            b.pop(0)
        else:
            b.pop(findHigher(b,a[-1]))
            a.pop(-1)
    return a_wins

def all_greater(a,b):
    for i in xrange(len(a)):
        if b[i] > a[i]:
            return False
    return True
def d_war(a,b):
    a, b = a[:], b[:]
    a.sort()
    b.sort()
    while True:
        if all_greater(a,b):
            return len(a)
        a.pop(0)
        b.pop(-1)
    return 0
        


    
caseNum = 1
with open('results.txt','w') as file:
    for test in testCases:
        file.write('Case #{}: {} {}\n'.format(caseNum,d_war(test[0],test[1])
                                              ,war(test[0],test[1])))
        caseNum += 1
    
