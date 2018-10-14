def hasWon():
    n_tests = int(raw_input())
    for i in range(n_tests):
        matrix = []
        for j in range(4):
            matrix.append(list(raw_input()))
        if letterHasWon(matrix,'X'):
            print('Case #'+str(i+1)+': X won')
        elif letterHasWon(matrix,'O'):
            print('Case #'+str(i+1)+': O won')
        elif (notCompleted(matrix)):
            print('Case #'+str(i+1)+': Game has not completed')
        else:
            print('Case #'+str(i+1)+': Draw')
        if i < n_tests-1:
            raw_input()
            
            
def letterHasWon(matrix,letter):
    for l in range(4):
        if  (matrix[l][0]==letter or matrix[l][0]=='T') and (matrix[l][1]==letter or matrix[l][1]=='T') and (matrix[l][2]==letter or matrix[l][2]=='T') and (matrix[l][3]==letter or matrix[l][3]=='T'):  
            return True
            
        elif (matrix[0][l]==letter or matrix[0][l]=='T') and (matrix[1][l]==letter or matrix[1][l]=='T') and (matrix[2][l]==letter or matrix[2][l]=='T') and (matrix[3][l]==letter or matrix[3][l]=='T'):  
            return True
        
        elif (matrix[0][0]==letter or matrix[0][0]=='T') and (matrix[1][1]==letter or matrix[1][1]=='T') and (matrix[2][2]==letter or matrix[2][2]=='T') and (matrix[3][3]==letter or matrix[3][3]=='T'):  
            return True
            
        elif (matrix[0][3]==letter or matrix[0][3]=='T') and (matrix[1][2]==letter or matrix[1][2]=='T') and (matrix[2][1]==letter or matrix[2][1]=='T') and (matrix[3][0]==letter or matrix[3][0]=='T'):  
            return True
            
    return False
            
def notCompleted(matrix):
    for l in range(4):
        if '.' in matrix[l]:
            return True
    return False            
    
hasWon()
