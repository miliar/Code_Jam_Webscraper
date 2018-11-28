def jamImport(str): 
    f= open(str,'r')
    data = f.read()
    f.close()
    return data.split('\n')

def str2list(str):
    return map(int, str.split())

data = jamImport('A-small-attempt0.in.txt')
numCases = int(data[0])
resFile = open('solutionA.txt','w')
 
for ele in range(1,numCases+1):
    row1 = int(data[1+ 10*(ele-1)])
    row2 = int(data[6+ 10*(ele-1)]) 
    res = set(str2list(data[1+row1+10*(ele-1)])) & set(str2list(data[6+row2+10*(ele-1)]))
    n = len(res)
    if n == 1: 
        resFile.write('Case #'+str(ele)+': '+str( next(iter(res)) ) + '\n' )
    elif n > 1: 
        resFile.write('Case #'+str(ele)+': ' + 'Bad magician!\n')
    elif n == 0: 
        resFile.write('Case #'+str(ele)+': ' + 'Volunteer cheated!\n') 

resFile.close()
