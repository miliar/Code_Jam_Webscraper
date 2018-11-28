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

    line = data_in.readline().split(' ')

    N=int(line[0])
    M=int(line[1])
    
    i=0
    C=[]
    while(i<N):
        j=0
        row=[]
        line = data_in.readline().split(' ')
        while(j<M):
            row.append( int(line[j]) )
            j+=1
        C.append( row )
        i+=1

       
#    print('C:', C)
#    print('F:', F)
#    print('b:', b)
#    print('p:', p)
#    print('points_list:', points_list)
    return(N,M,C)

def calculate_result(N,M,C):

    #calculate row max
    i=0
    row_max=[]
    while i< N:
        j=0
        maxi=0
        while j < M:
            if C[i][j] > maxi:
                maxi=C[i][j]
            j+=1
        row_max.append (maxi)
        i+=1

    #calculate col max
    col_max=[]
    j=0
    while j < M:
        maxi=0
        i=0
        while i < N:
            if C[i][j] > maxi:
                maxi=C[i][j]
            i+=1
        col_max.append(maxi)
        j+=1

    i=0
    j=0
    while(i<N):
        j=0
        while j < M:
            if C[i][j]<row_max[i] and C[i][j]<col_max[j]:
                return 'NO'
            j+=1
        i+=1
 
#    print('row_max:', row_max)    
#    print('col_max:', col_max)       
    result='YES'
    return result

      

       
(data_in, data_out) = initialize()
no_test_cases = int( data_in.readline() )

i = 0
while ( i < no_test_cases ):
    i+=1
    N,M,C = get_variables()
    if(i==99):
        j=i
#        help('str')
    result = calculate_result(N,M,C)
    print( 'Case #' + str(i) + ': ' + str(result) )
    data_out.write( 'Case #' + str(i) + ': ' + str(result) + '\n' )
    


