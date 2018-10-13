def SelectNextServer(query_list, serv_list):
    #print "Query List = " + str(query_list) + "\nServer List = " + str(serv_list)
    engines_marking = []
    index = 0
    for serv in serv_list:
        engines_marking.append(1000+index)
        index += 1
        
    index = 0
    for query in query_list:        
        eng_index  = serv_list.index(query)
        if engines_marking[eng_index] >= 1000:
            engines_marking[eng_index] = index+1            
        index += 1
    
    maximum = max(engines_marking)
    return engines_marking.index(maximum)
        

def prepare_input(input_file):
    test_case_count = int(input_file.readline())  #number of test cases
    test_case_engine = []
    test_case_query = []
    engines_marking = []
    output_file = file("A-large.out", "w")
    
    for test_case_counter in xrange(test_case_count):

        engines_count = int(input_file.readline()) #engines count
        #get all the engines
        engines = []        
        for i in range(engines_count):
            engines.append(input_file.readline().replace('\n',''))      
        query_count = int(input_file.readline()) #query count for the above engines
        #get queries
        queries = []
        for j in range(query_count):
            queries.append(input_file.readline().replace('\n',''))
                   
        curr_serv = engines[SelectNextServer(queries,engines)]
        
        switch = 0
        for j in range(query_count):
            if curr_serv == queries[j]:
                curr_serv = engines[SelectNextServer(queries[j:],engines)]
                switch += 1               
        
            
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+": "+ str(switch)+"\n") 

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("A-large.in")
    prepare_input(input_file)
