import sys

def initialize():
    file_in = 'D:\code jam\input.in'
    file_out = 'D:\code jam\output.txt'
    
    try:
        data_in  = open(file_in, 'r')
    except:
        print("Can't open file \'" + data_in +"\'")
        sys.exit()
    
    try:
        data_out  = open(file_out, 'w')
    except:
        print("Can't write to file \'" + data_out +"\'")
        sys.exit()

    return(data_in, data_out)

def get_variables():

#    line = data_in.readline().split(' ')

    matrix=[]
    i=0
    while(i<4):
        line = data_in.readline()
        matrix.append(line)
        i+=1

    line = data_in.readline()     
#    print('C:', C)
#    print('F:', F)
#    print('b:', b)
#    print('p:', p)
#    print('matrix:', matrix)
    return(matrix)

def calculate_result(matrix):
    #Horizontal
    i=0
    while(i<4):
        j=0
        count=0
        while(j<4):
            if matrix[i][j]=='O' or matrix[i][j]=='T':
                count+=1
            else:
                break
            if count==4:
                return 'O won'
            j+=1

        j=0
        count=0
        while(j<4):        
            if matrix[i][j]=='X' or matrix[i][j]=='T':
                count+=1
            else:
                break
            if count==4:
                return 'X won'
            j+=1
        i+=1

    #Vertical
    i=0
    while(i<4):
        j=0
        count=0
        while(j<4):
            if matrix[j][i]=='O' or matrix[j][i]=='T':
                count+=1
            else:
                break
            if count==4:
                return 'O won'
            j+=1

        j=0
        count=0
        while(j<4):        
            if matrix[j][i]=='X' or matrix[j][i]=='T':
                count+=1
            else:
                break
            if count==4:
                return 'X won'
            j+=1
        i+=1               

    #Diagonals
    i=0
    count=0
    while(i<4):
        if matrix[i][i]=='O' or matrix[i][i]=='T':
            count+=1
        else:
            break
        if count==4:
            return 'O won'
        i+=1

    i=0
    count=0
    while(i<4):
        if matrix[i][i]=='X' or matrix[i][i]=='T':
            count+=1
        else:
            break
        if count==4:
            return 'X won'
        i+=1

    i=0
    count=0        
    while(i<4):
        if matrix[i][3-i]=='O' or matrix[i][3-i]=='T':
            count+=1
        else:
            break
        if count==4:
            return 'O won'
        i+=1

    i=0
    count=0
    while(i<4):
        if matrix[i][3-i]=='X' or matrix[i][3-i]=='T':
            count+=1
        else:
            break
        if count==4:
            return 'X won'
        i+=1        

    #Finished?        
    i=0
    while(i<4):
        j=0
        while(j<4):
            if matrix[i][j]=='.':
                return 'Game has not completed'
            j+=1
        i+=1

    result='Draw'
    return result

 
       
(data_in, data_out) = initialize()
no_test_cases = int( data_in.readline() )

i = 0
while ( i < no_test_cases ):
    i+=1
    matrix = get_variables()
    if(i==99):
        j=i
#        help('str')
    result = calculate_result(matrix)
    print( 'Case #' + str(i) + ': ' + str(result) )
    data_out.write( 'Case #' + str(i) + ': ' + str(result) + '\n' )
    


