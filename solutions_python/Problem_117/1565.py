

def read_words(filename):
    '''
    converts a file to a list
    '''
    
    words = []
    for line in filename:
            words.append(line.split())
    return words

def test_matrix(matrix, N, M):
    totalfalse = 0
    for i in range(N):
        for j in range(M):
            if int(matrix[i][j])==1:
                for k in range(M):
                    if int(matrix[i][k]) ==2: #row check
                        for l in range(N):
                            if int(matrix[l][j])==2: #column check
                                return "NO"      
    return "YES"
        
filename = open("testB1.txt", "r")
T= int(filename.readline())
readings = read_words(filename)

for Lawn in range(int(T)):
    dimensions = readings[0]
    N = int(dimensions[0])
    M = int(dimensions[1])
    matrix = readings[1:N+1]
    print "Case #"+(str(Lawn+1))+": "+test_matrix(matrix, N, M)
                

    readings = readings[N+1:]

filename.close()