def get_min_scalar(v1, v2, n):
    answer = 0
    v1.sort()
    v2.sort()
    v2.reverse()
    for i in range(n):
        answer += v1[i] * v2[i]
    return answer
        

def prepare_input(input_file):
    test_case_count = int(input_file.readline())  #number of test cases
    
    output_file = file("A-large.out", "w")
    
    for test_case_counter in xrange(test_case_count):

        n = int(input_file.readline()) #integer count
        #get all the engines
        v1 = []
        v2 = []
        lines1 = (input_file.readline().replace('\n','')).split(' ')
        for i in range(n):
            v1.append(int(lines1[i]))
            
        lines2 = (input_file.readline().replace('\n','')).split(' ')
        i = 0
        for i in range(n):
            v2.append(int(lines2[i]))
        
        out_put = get_min_scalar(v1,v2, n)        
        
            
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+": "+ str(out_put)+"\n") 

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("A-large.in")
    prepare_input(input_file)
