FILE_NAME = 'A-small-attempt0.in'


numCases = 0
testCases = []
with open(FILE_NAME,'r') as file:
    numCases = int(file.readline())
    for case in xrange(numCases):
        testCases.append([])
        testCases[case].append(int(file.readline()))
        testCases[case].append([])
        for e in xrange(4):
            testCases[case][1].append(file.readline().split())
        testCases[case].append(int(file.readline()))
        testCases[case].append([])
        for e in xrange(4):
            testCases[case][3].append(file.readline().split())
            

def magic_trick(pick1,grid1,pick2,grid2):
     picka = set(grid1[pick1-1])
     pickb = set(grid2[pick2-1])
     unique = picka.intersection(pickb)
     if len(unique) == 1: return int(list(unique)[0])
     if len(unique) > 1: return 'Bad magician!'
     if len(unique) == 0: return 'Volunteer cheated!' 
    
    

    
    

caseNum = 1
with open('results.txt','w') as file:
    for test in testCases:
        file.write('Case #{}: {}\n'.format(caseNum,magic_trick(test[0],test[1],test[2],test[3])))
        caseNum += 1
    

