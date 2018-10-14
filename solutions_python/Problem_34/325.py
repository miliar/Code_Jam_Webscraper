import re

def convertToRE(v1):
    v2 = v1.replace('(','[').replace(')',']')
    return v2
        

def prepare_input(input_file):
    inp_list = (input_file.readline().replace('\n','')).split(' ')
    L = int(inp_list[0])
    D = int(inp_list[1])
    N = int(inp_list[2]) #integer count
    
    output_file = file("A-large.out", "w")
    dict=[]
    
    for i in xrange(D):
        dict.append(input_file.readline().replace('\n',''));
        
    for test_case_counter in xrange(N):
        result_count=0
        #get all the engines
        v1 = input_file.readline().replace('\n','')
                
        v2 = convertToRE(v1)
        pattern = re.compile(v2)
        
        for i in xrange(len(dict)):
            match_group = pattern.match(dict[i])
            try:
                match_group.group()
                result_count += 1
            except:
                continue
           
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+": "+ str(result_count)+"\n") 

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("A-large.in")
    prepare_input(input_file)
