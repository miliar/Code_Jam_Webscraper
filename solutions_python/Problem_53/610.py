#import math

def prepare_input(input_file):
    T = int(input_file.readline().replace('\n',''))
        
    output_file = file("A-large.out", "w")
        
    for test_case_counter in xrange(T):
        result_count=0
        #get all the engines
        v1 = input_file.readline().replace('\n','').split(' ')
        N = int(v1[0])
        K = int(v1[1])
        result = "OFF"      
        v2 = (K+1)%pow(2,N)
        if v2 == 0:
          result = "ON"
                                      
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+": "+ str(result)+"\n") 

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("A-large.in")
    prepare_input(input_file)
