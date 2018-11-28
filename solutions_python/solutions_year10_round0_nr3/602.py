#import math
def getSum(N, v2):
    ret_val = 0
    for i in xrange(N):
        ret_val = ret_val+int(v2[i])
    return ret_val
    
def getEuros(R,k, N, v2):
    money = 0
    index = 0
    sum_all = getSum(N, v2)
    if sum_all <= k:
        return sum_all*R
        
    for i in xrange(R):
        people_on_board = 0
        while people_on_board+int(v2[index]) <= k:
            people_on_board = people_on_board + int(v2[index])
            index = (index + 1)%N 
        money = money + people_on_board
         
    
    return money
    
def prepare_input(input_file):
    T = int(input_file.readline().replace('\n',''))
        
    output_file = file("C-small-attempt0.out", "w")
        
    for test_case_counter in xrange(T):
        result_count=0
        #get all the engines
        v1 = input_file.readline().replace('\n','').split(' ')
        R = int(v1[0])
        k = int(v1[1])
        N = int(v1[2])
        v2 = input_file.readline().replace('\n','').split(' ')
        result = getEuros(R,k, N, v2)
                                      
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+": "+ str(result)+"\n") 

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("C-small-attempt0.in")
    prepare_input(input_file)
