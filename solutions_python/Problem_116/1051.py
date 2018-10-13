

# -*- coding: utf-8 -*-

    

def jobRun(matrix):
    ''' 10 Win cases: row cases: 4, column cases: 4, crossingline cases: 2
        resCases = ['X won', 'O won', 'Draw', 'Game has not completed']
    '''
    
    ### check row cases
    XwinCases = [set(['X']), set(['X', 'T'])]
    OwinCases = [set(['O']), set(['O', 'T'])]
    for row in matrix:
        s = set(row)
        if s in XwinCases:
            return 'X won'
        elif s in OwinCases:
            return 'O won'
            
    ### check column cases
    for i in xrange(4):
        s = set([matrix[0][i],matrix[1][i],matrix[2][i],matrix[3][i]])
        if s in XwinCases:
            return 'X won'
        elif s in OwinCases:
            return 'O won'
    
    ### check crossingline cases
    s = set([matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3]])
    if s in XwinCases:
        return 'X won'
    elif s in OwinCases:
        return 'O won'
        
    s = set([matrix[0][3], matrix[1][2], matrix[2][1], matrix[3][0]])
    if s in XwinCases:
        return 'X won'
    elif s in OwinCases:
        return 'O won'
    
    for i in xrange(4):
        for j in xrange(4):
            if matrix[i][j] == '.':
                return 'Game has not completed'
    return 'Draw'


def getinput(inputSize):
    file = r'C:\ewy\A-{inputSize}.in'.format(inputSize=inputSize)
    return open(file, 'r')

def saveoutput(inputSize, results):
    resFile = r'C:\ewy\A-{inputSize}.out'.format(inputSize=inputSize)
    with open(resFile, 'w') as f:
        f.writelines(results)



def main():
    inputSize = 'large'
    f = getinput(inputSize)
    with f:
        N = int(f.readline())
        print 'N:', N
        
        resLines = ''
        for case in range(1,N+1):
            line1 = list(f.readline().strip())
            line2 = list(f.readline().strip())
            line3 = list(f.readline().strip())
            line4 = list(f.readline().strip())
            whiteLine = f.readline()
            
            matrix = [line1, line2, line3, line4]
            
            # print matrix
            res = jobRun(matrix)
        
            resLine = 'Case #{case}: {res}'.format(case=case, res=res)
            print resLine
            resLines +=resLine + '\n'
            
    saveoutput(inputSize, resLines)