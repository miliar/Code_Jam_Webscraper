def mark_all(input_matrix, output_matrix, H, W):
    for i in xrange(H):
        for j in xrange(W):
            mark_all_in_path(input_matrix, output_matrix, i,j, H, W, output_matrix[i][j])
            
        
init_char = 97
        
def get_next_char():
    global init_char
    init_char += 1
    return chr(init_char)

def reset_next_char():
    global init_char
    init_char = 97
    
def mark_all_in_path(input_matrix, output_matrix, i,j, H, W, mark_char):
    least_i, least_j = find_least_neighbour(input_matrix, i,j, H, W)
    #print i, j, least_i, least_j
    sink_mark = '0'
    if least_i != i or least_j != j:
        if output_matrix[least_i][least_j] == '0':
            sink_mark = mark_all_in_path(input_matrix, output_matrix, least_i,least_j, H, W, mark_char)
        else:
            sink_mark = output_matrix[least_i][least_j]
    else:
        if mark_char == '0':
            if sink_mark == '0':
                sink_mark = output_matrix[i][j]
            if sink_mark == '0':
                sink_mark = get_next_char()
        else:
            sink_mark = mark_char
    output_matrix[i][j] = sink_mark
    return sink_mark
    
def find_least_neighbour(input_matrix, i,j, H, W):
    least_i = i
    least_j = j
    if i+1 < H and input_matrix[least_i][least_j] > input_matrix[i+1][j]:
        least_i = i+1
        least_j = j
    
    if least_i != i or least_j != j:
        if j+1 < W and input_matrix[least_i][least_j] >= input_matrix[i][j+1]:
            least_i = i
            least_j = j+1
    else:
        if j+1 < W and input_matrix[least_i][least_j] > input_matrix[i][j+1]:
            least_i = i
            least_j = j+1
    
    if least_i != i or least_j != j:
        if j-1 >= 0 and input_matrix[least_i][least_j] >= input_matrix[i][j-1]:
            least_i = i
            least_j = j-1
    else:
        if j-1 >= 0 and input_matrix[least_i][least_j] > input_matrix[i][j-1]:
            least_i = i
            least_j = j-1
            
    if least_i != i or least_j != j:
        if i-1 >= 0 and input_matrix[least_i][least_j] >= input_matrix[i-1][j]:
            least_i = i-1
            least_j = j
    else:
        if i-1 >= 0 and input_matrix[least_i][least_j] > input_matrix[i-1][j]:
            least_i = i-1
            least_j = j
    return least_i, least_j
    
def prepare_input(input_file):
    test_case_count = int(input_file.readline())  #number of test cases
    
    output_file = file("B-large.out", "w")
    
    for test_case_counter in xrange(test_case_count):

        input_matrix = []
        output_matrix = []
        lines1 = (input_file.readline().replace('\n','')).split(' ')
        H = int(lines1[0])
        W = int(lines1[1])
        
        for i in xrange(H):
            temp2=[]
            temp3=[]
            for j in xrange(W):
                temp2.append('0')
            output_matrix.append(temp2)
            temp=(input_file.readline().replace('\n','')).split(' ')
            for j in xrange(W):
                temp3.append(int(temp[j]))
            input_matrix.append(temp3)
        output_matrix[0][0] = 'a'
        mark_all(input_matrix, output_matrix, H, W)
        
        reset_next_char()    
        #lowest count will be the number of switches in the server
        output_file.write("Case #"+str(test_case_counter+1)+":\n")
        for i in xrange(H):
            for j in xrange(W):
                output_file.write(str(output_matrix[i][j]) + " ");
            output_file.write("\n")
            
    output_file.close()
    
if __name__ == "__main__":
    input_file = file("B-large.in")
    prepare_input(input_file)
