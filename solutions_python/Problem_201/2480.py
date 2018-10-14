
def setup_stalls(num_stalls):
    output = []
    output.append([-1,-1])
    for i in range(0,num_stalls):
        output.append([i,num_stalls-i-1])
    output.append([-1,-1])
    return output

def find_best_stall_1st_pass(stalls_array):
    current_max = -1
    saved_index_array = []
    for i in range(0,len(stalls_array)):
        if min(stalls_array[i]) != -1:
            #print min(stalls_array[i]), current_max
            if min(stalls_array[i]) == current_max:
                saved_index_array.append(i)
            elif min(stalls_array[i]) > current_max:
                current_max = min(stalls_array[i])
                saved_index_array = [i]
    return saved_index_array

def stall_slice(stalls_array,index_array):
    output = []
    for index in index_array:
        output.append(stalls_array[index])
    return output

def find_best_stall_2nd_pass(stalls_array,index_array):
    current_max = -1
    saved_index_array = []
    for i in index_array:
        if max(stalls_array[i]) != -1:
            #print min(stalls_array[i]), current_max
            if max(stalls_array[i]) == current_max:
                saved_index_array.append(i)
            elif max(stalls_array[i]) > current_max:
                current_max = max(stalls_array[i])
                saved_index_array = [i]
    return saved_index_array

def find_next_right(stalls_array,current_index):
    count = 0
    for i in range(current_index+1,len(stalls_array)):
        if min(stalls_array[i]) == -1:
            "Found person!"
            return count
        else:
            count += 1

def find_next_left(stalls_array,current_index):
    count = 0
    for i in range(current_index-1,-1,-1):
        if min(stalls_array[i]) == -1:
            return count
        else:
            count += 1
    
def update_stalls(stalls_array):
    for i in range(1,len(stalls_array)):
        if min(stalls_array[i]) != -1:
            
            left = find_next_left(stalls_array,i)
            #print "Left: ",left
            right = find_next_right(stalls_array,i)
            #print "Right: ", right
            output = [left,right]
            
            stalls_array[i] = output
    return stalls_array

def insert_person(stalls_array,index):
    output = stalls_array[index]
    stalls_array[index] = [-1,-1]
    return stalls_array,output

f = open('C-small-1-attempt2.in')

w = open('q3-output.txt','w')

f.readline()
count = 1
for line in f:
    print "Starting Case #: " + str(count)
    output_prefix = "Case #" + str(count) + ": "
    line_array = line.strip().split()
    num_stalls = int(line_array[0])
    num_people = int(line_array[1])

    if num_people > 1 and num_people%2 == 0:
        num_stalls = num_stalls/2
        num_people = num_people/2

    stalls_array = setup_stalls(num_stalls)
    
    #print stalls_array

    for i in range(0,num_people):
        index_array = find_best_stall_1st_pass(stalls_array)
        #print "Best stall, ",index_array
        if len(index_array) == 1:
            index = index_array[0]
        else:
            index_array = find_best_stall_2nd_pass(stalls_array,index_array)
            #print "Best stall, ",index_array
            index = index_array[0]
        if index_array == []:
            index = 0
        if i == num_people-1:
            stalls_array = update_stalls(stalls_array) 
        stalls_array,output = insert_person(stalls_array,index)
        stalls_array = update_stalls(stalls_array)
        #print stalls_array
       
    w.write(output_prefix + str(max(output)) + " " + str(min(output)) + "\n")
    count += 1
    stalls_array = []
    index_array = []
        

w.close()
f.close()

print "DONE"
