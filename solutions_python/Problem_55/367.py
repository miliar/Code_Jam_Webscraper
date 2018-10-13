#import math
def getSum(N, v2):
    ret_val = 0
    for i in xrange(N):
        ret_val = ret_val+int(v2[i])
    return ret_val

def generate_map(k,N,v2):
    d = {}
    for i in xrange(N):
        people_on_board = 0
        index = i
        while people_on_board+int(v2[index]) <= k:
            people_on_board = people_on_board + int(v2[index])
            index = (index + 1)%N
        d[i] = [people_on_board,index]
    return d
            
def getEuros(R,k, N, v2):
    print "***************************"
    print R, k, N
    money = 0
    index = 0
    sum_all = getSum(N, v2)
    visited = []
    first_time = 1
    count = 0
    if sum_all <= k:
        return sum_all*R
    i = 1
    dic = generate_map(k, N, v2)
    while i <= R:
        val = dic[index]
        money = money + val[0]
        index = val[1]
        #if index in visited:            
            #if first_time == 1:
              #print "Visited: " + str(visited) + " visited index = " + str(index)
              #first_time = 0
              #times = R/i
              #print "R = " + str(R) + "old i = " + str(i)
              #i = times*i - 1
              #print times, i
              #money = money*times
        #else:
            #visited.append(index)
        count = count + 1
        i=i+1
    print "loop count = " + str(count)
    return money
    
def prepare_input(input_file):
    T = int(input_file.readline().replace('\n',''))
        
    output_file = file("C-large1.out", "w")
        
    for test_case_counter in xrange(T):
        v1 = input_file.readline().replace('\n','').split(' ')
        R = int(v1[0])
        k = int(v1[1])
        N = int(v1[2])
        v2 = input_file.readline().replace('\n','').split(' ')
        result = getEuros(R,k, N, v2)
        output_file.write("Case #"+str(test_case_counter+1)+": "+ str(result)+"\n") 

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("C-large.in")
    prepare_input(input_file)
