def make_matrix():
    matrix = []
    for i in range(4):
        line = raw_input()
        line = list(line)
        matrix.append(line)
    return matrix

def analize_matrix(matrix):
    output = 'Draw'
    
    #check diagonal for X
    if((matrix[0][0] == 'X' or matrix[0][0] == 'T') and
       (matrix[1][1] == 'X' or matrix[1][1] == 'T') and
       (matrix[2][2] == 'X' or matrix[2][2] == 'T') and
       (matrix[3][3] == 'X' or matrix[3][3] == 'T')):
        output = 'X won'
        return output
        
    #check diagonal for O
    if((matrix[0][0] == 'O' or matrix[0][0] == 'T') and
       (matrix[1][1] == 'O' or matrix[1][1] == 'T') and
       (matrix[2][2] == 'O' or matrix[2][2] == 'T') and
       (matrix[3][3] == 'O' or matrix[3][3] == 'T')):
        output = 'O won'
        return output
        
    #check the other diagonal for X
    if((matrix[0][3] == 'X' or matrix[0][3] == 'T') and
       (matrix[1][2] == 'X' or matrix[1][2] == 'T') and
       (matrix[2][1] == 'X' or matrix[2][1] == 'T') and
       (matrix[3][0] == 'X' or matrix[3][0] == 'T')):
        output = 'X won'
        return output
        
    #check the other diagonal for O
    if((matrix[0][3] == 'O' or matrix[0][3] == 'T') and
       (matrix[1][2] == 'O' or matrix[1][2] == 'T') and
       (matrix[2][1] == 'O' or matrix[2][1] == 'T') and
       (matrix[3][0] == 'O' or matrix[3][0] == 'T')):
        output = 'O won'
        return output

    for k in range(4):
        #check line for X
        if((matrix[k][0] == 'X' or matrix[k][0] == 'T') and
           (matrix[k][1] == 'X' or matrix[k][1] == 'T') and
           (matrix[k][2] == 'X' or matrix[k][2] == 'T') and
           (matrix[k][3] == 'X' or matrix[k][3] == 'T')):
            output = 'X won'
            return output
        
        #check colum for X
        if((matrix[0][k] == 'X' or matrix[0][k] == 'T') and
           (matrix[1][k] == 'X' or matrix[1][k] == 'T') and
           (matrix[2][k] == 'X' or matrix[2][k] == 'T') and
           (matrix[3][k] == 'X' or matrix[3][k] == 'T')):
            output = 'X won'
            return output

        #check line for O
        if((matrix[k][0] == 'O' or matrix[k][0] == 'T') and
           (matrix[k][1] == 'O' or matrix[k][1] == 'T') and
           (matrix[k][2] == 'O' or matrix[k][2] == 'T') and
           (matrix[k][3] == 'O' or matrix[k][3] == 'T')):
            output = 'O won'
            return output
        
        #check colum for O
        if((matrix[0][k] == 'O' or matrix[0][k] == 'O') and
           (matrix[1][k] == 'O' or matrix[1][k] == 'O') and
           (matrix[2][k] == 'O' or matrix[2][k] == 'O') and
           (matrix[3][k] == 'O' or matrix[3][k] == 'O')):
            output = 'O won'
            return output
            
    
    #check if game has not completed
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] == '.'):
                output = 'Game has not completed'
                
    return output

def print_output(i, output):
    print 'Case #' + str(i+1) + ': ' + output
    
##############################################
n_cases = input()

for i in range(n_cases):
    matrix = make_matrix()
    output = analize_matrix(matrix)
    print_output(i,output)
    nothing = raw_input()
