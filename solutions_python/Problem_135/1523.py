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

    A = int( data_in.readline() )
    line1=[]
    for i in range(1,5):
        line = data_in.readline().split(' ')
        if i == A:
            for j in range(0,4):
                line1.append( int(line[j]) )

    A = int( data_in.readline() )
    line2=[]
    for i in range(1,5):
        line = data_in.readline().split(' ')
        if i == A:
            for j in range(0,4):
                line2.append( int(line[j]) )


#    print('line1:', line1)
#    print('line2:', line2)
#    print('l:', l)
#    print('points_list:', points_list)
    return(line1,line2)


def calculate_result(line1,line2):
    result = "Volunteer cheated!"
    
    for  i in range(0,4):
        for j in range(0,4):
            if line1[i]==line2[j]:
                if result=="Volunteer cheated!":
                    result = line1[i]
                else:
                    return "Bad magician!"
                
    return result
        


(data_in, data_out) = initialize()
no_test_cases = int( data_in.readline() )

i = 0
while ( i < no_test_cases ):
    i+=1
    (line1,line2) = get_variables()
    if(i==3):
        j=i
#        help('str')
    result = calculate_result(line1,line2)
    print( 'Case #' + str(i) + ': ' + str(result) )
    data_out.write( 'Case #' + str(i) + ': ' + str(result) + '\n' )

    


