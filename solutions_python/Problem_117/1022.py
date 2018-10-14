

# -*- coding: utf-8 -*-

    

def jobRunSmall(matrix, N, M):
    ''' No internal element lower than outer layers
    '''
    if '1' not in str(matrix):
        return 'YES'
    else:
        for line in matrix:
            if '1' in line and '2' in line:
                for i in xrange(M):
                    if line[i] == '1':
                        colItems = [matrix[j][i] for j in xrange(N)]
                        if '2' in colItems:
                            return 'NO'
        return 'YES'
                        
                                                  
def jobRun(matrix, N, M):
    ''' No internal element lower than outer layers
    '''
    
    for line in matrix:
        line = [int(i) for i in line]
        maxRow = max(line)
        for col in xrange(M):
            if line[col]<maxRow:
                colItems = [int(matrix[j][col]) for j in xrange(N)]
                maxCol = max(colItems)
                if line[col] < maxCol:
                    return 'NO'
    return 'YES'
        

def getinput():
    file = r'C:\ewy\B-large.in'
    return open(file, 'r')

def saveoutput(results):
    resFile = r'C:\ewy\B-large.out'
    with open(resFile, 'w') as f:
        f.writelines(results)



def main():

    f = getinput()
    with f:
        N = int(f.readline())
        print 'N:', N
        
        resLines = ''
        for case in range(1,N+1):
            
            [N, M] = f.readline().strip().split()
            N, M = int(N), int(M)
            
            matrix = list()
            for row in xrange(N):
                line = f.readline().strip().split()
                assert(len(line) == M)
                matrix.append(line)
            
            # print matrix
            
            res = jobRun(matrix, N, M)
        
            resLine = 'Case #{case}: {res}'.format(case=case, res=res)
            print resLine
            resLines +=resLine + '\n'
            
    saveoutput(resLines)