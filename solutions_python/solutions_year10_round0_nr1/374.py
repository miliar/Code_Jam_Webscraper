
def parse_file(input_file):
    T = int(input_file.readline().replace('\n',''))        
    out_file = file("A-large-attempt0.out", "w")        
    for counter in xrange(T):
        list1 = input_file.readline().replace('\n','').split(' ')
        N = int(list1[0])
        K = int(list1[1])
        result = "OFF"      
        v2 = (K+1)%pow(2,N)
        if v2 == 0:
          result = "ON"
                                      
        out_file.write("Case #"+str(counter+1)+": "+ str(result)+"\n") 

    out_file.close()
    
if __name__ == "__main__":
    input_file = file("A-large.in")
    parse_file(input_file)
