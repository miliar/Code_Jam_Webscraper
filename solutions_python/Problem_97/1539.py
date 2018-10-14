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
    L = len( line[0] )
    A = int( line[0] )
    B = int( line[1] )

#    print('A:', A)
#    print('B:', B)
#    print('L:', L)
    return(A,B,L)

def calculate_result(A,B,L):
    test = A
    pairs=0  
    pair_list=[] 
    
    while(test<B):
        i=1
        test_string = str(test)
        while(i<L):
            i+=1
            test_string = test_string[1:]+test_string[0]
            possible_pair = int(test_string)
            if(possible_pair>test and possible_pair<=B):
                test_string2 = str(test) + test_string
                if (test_string2 in pair_list):
                    continue
                else:
                    pair_list.append(test_string2)
                    pairs+=1
        
        test+=1
        
    #print('pair_list:', pair_list)
    return pairs

   
(data_in, data_out) = initialize()
no_test_cases = int( data_in.readline() )

i = 0
while ( i < no_test_cases ):
    i+=1
    A,B,L = get_variables()
#    if(i==1):
#        help('str')
    result = calculate_result(A,B,L)
    print( 'Case #' + str(i) + ': ' + str(result) )
    data_out.write( 'Case #' + str(i) + ': ' + str(result) + '\n' )
    


