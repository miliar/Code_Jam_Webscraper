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
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    
#    print('C:', C)
#    print('F:', F)
#    print('sizes:', sizes)
#    print('X:', X)
#    print('points_list:', points_list)
    return(C,F,X)




def calculate_result(C,F,X):
    N=0
    total=0
    
    t_farm = time_farm(C,F,X,N)
    t_goal = time_goal(C,F,X,N)
    t_goal_next=time_goal(C,F,X,N+1)
 
    while (t_farm + t_goal_next < t_goal):
        total += t_farm
        N+=1
        t_farm = time_farm(C,F,X,N)
        t_goal = time_goal(C,F,X,N)
        t_goal_next=time_goal(C,F,X,N+1)
    
    total += t_goal   
    return total

def time_goal(C,F,X,N):
    return X / (2 + N * F)
  
def time_farm(C,F,X,N):
    return C / (2 + N * F)
  
(data_in, data_out) = initialize()
no_test_cases = int( data_in.readline() )

i = 0
while ( i < no_test_cases ):
    i+=1
    (C,F,X) = get_variables()
    if(i==99):
        j=i
#        help('str')
    result = calculate_result(C,F,X)
    print( 'Case #' + str(i) + ': ' + "%.7f" % round(result,7) )
    data_out.write( 'Case #' + str(i) + ': ' + "%.7f" % round(result,7) + '\n' )
    


