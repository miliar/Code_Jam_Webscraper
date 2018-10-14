def isPossible():
    n_tests = int(raw_input())
    for n_test in range(n_tests):
        nm = raw_input().split(' ')
        n = int(nm[0])
        m = int(nm[1])
        matrix = []
        for i in range(n):
            lista = [int(x) for x in raw_input().split(' ')]
            matrix.append(lista)
        if isValid(matrix,n,m):
            print('Case #'+str(n_test+1)+': YES')
        else:
            print('Case #'+str(n_test+1)+': NO')
        
         
def isValid(matrix,n,m):
    #pra cada linha, pega as posicoes minimas
    #pra cada posicao minima, ve se tal elemento eh o maior da sua linha ou coluna
    for i in range(n):
        minpositions = findminpositions(matrix[i])
        for pos in minpositions:
            if not isgreater(matrix,i,pos):
                return False
    #pra cada coluna, pega as posicoes minimas
    #pra cada posicao minima, ve se tal elemento eh o maior da sua linha ou coluna
    for i in range(m):
        col = getcol(matrix,i)
        minpositions = findminpositions(col)
        for pos in minpositions:
            if not isgreater(matrix,pos,i):
                return False
    return True
    
def findminpositions(array):
    minpositions=[0]
    minv = 100
    for i in range(len(array)):
        if array[i]<minv:
            minv=array[i]
            minpositions=[i]
        elif array[i]==minv:
            minpositions.append(i)
    return minpositions
    
def getcol(matrix,i):
    col = []
    for j in range(len(matrix)):
        col.append(matrix[j][i])
    return col
    
def isgreater(matrix,lin,col):
    elt = matrix[lin][col]
    greater_of_line = True
    greater_of_col = True
    for i in matrix[lin]:
        if i>elt:
            greater_of_line = False
            break
    for i in getcol(matrix,col):
        if i>elt:
            greater_of_col = False
            break
    return greater_of_line or greater_of_col
    
isPossible()
