#Tom Dobrow
#Google Code Jam
#4-13-2013

def read_words(afile):
    words = []
    for line in afile:
            words.append(line.split())
    return words

def test(mat, N, M):
    for i in range (N):
        for j in range (M):
            boolean = CheckColumn(mat, i, j)
            boolean2 = CheckRow(mat, i, j)
            if (boolean==False and boolean2==False):
                return False
    return True
    

def CheckColumn(matrix, i, j):
    for k in range(N):
        if int(matrix[k][j])>int(matrix[i][j]):
            return False
def CheckRow(matrix, i, j):
    for l in range(M):
        if int(matrix[i][l])>int(matrix[i][j]):
            return False
                        



filename = open('Tim.txt' , 'r')
T = filename.readline()
aList = read_words(filename)  #aList is a list with each element being the lines past the first

for Lawn in range(int(T)):
    dimension = aList[0]

    N = int(aList[0][0])
    M = int(aList[0][1])
    
    matrix = []
    for i in range(N):
        matrix.append(aList[i+1])
    
    
    aList = aList[N+1:]
    
    output = test(matrix, N, M) 
    if (output==True):
        output = 'YES'
    else:
        output = 'NO'
    print 'Case #' + str(Lawn+1) + ': ' + str(output)
    
filename.close()