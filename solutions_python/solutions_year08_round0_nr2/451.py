def extract_dep_arr(input_data, T):
    times = input_data.split(' ')
    dep = int(times[0].replace(':',''))
    arr = int(times[1].replace(':','')) + T
    return dep, arr

def extract_NA_NB(input_data):
    na_nb = input_data.split(' ')
    NA = int(na_nb[0]) 
    NB = int(na_nb[1]) 
    return NA, NB     

def find_closest_arrival(dep_time, arr_list):
    min = 10000
    index = -1
    i = 0;
    for arrival in arr_list:
        diff = dep_time - arrival
        if diff >= 0:
            min = diff
            index = i
            break
        i += 1
    return index
            
def prepare_input(input_file):
    test_case_count = int(input_file.readline())      
    output_file = file("B-small-attempt3.out", "w")
    
    for test_case_counter in xrange(test_case_count):
        T = int(input_file.readline())
        NA, NB = extract_NA_NB(input_file.readline().replace('\n','')) 
        
        arrival_A = [] 
        arrival_B = []
        dep_A = []
        dep_B = []
        for i in range(NA):
            dep, arr = extract_dep_arr(input_file.readline().replace('\n',''), T)
            dep_A.append(int(dep))
            arrival_B.append(int(arr)) 
        for i in range(NB):
            dep, arr = extract_dep_arr(input_file.readline().replace('\n',''), T)
            dep_B.append(int(dep))
            arrival_A.append(int(arr))
                
        arrival_A.sort()
        arrival_B.sort()
        dep_A.sort()
        dep_B.sort()
        
        temp_dep_A = []
        for entry in dep_A:
            temp_dep_A.append(entry)
            
        for dep_time in temp_dep_A:
            index = find_closest_arrival(dep_time, arrival_A)
            if index>=0:
                arrival_A.remove(arrival_A[index])
                dep_A.remove(dep_time)
        
       
        temp_dep_B = []
        for entry in dep_B:
            temp_dep_B.append(entry)
        for dep_time in temp_dep_B:
            index = find_closest_arrival(dep_time, arrival_B)
            if index>=0:
                arrival_B.remove(arrival_B[index])
                dep_B.remove(dep_time)
                
        NTA = len(dep_A)
        NTB = len(dep_B)
        #print arrival_A
        #print arrival_B
        #print dep_A
        #print dep_B
        #print "\n"
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+": "+ str(NTA) + " " +str(NTB) +"\n")
        
    output_file.close()
    
if __name__ == "__main__":
    input_file = file("B-small-attempt3.in")
    prepare_input(input_file)
