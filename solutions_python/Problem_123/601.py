def findAddOperationReq(mot_size, size):
    ops = 0
    while mot_size <= size:
        #print mot_size, size
        ops = ops + 1
        mot_size = mot_size + mot_size-1
    return ops, mot_size
    
def prepare_input(input_file):
    test_case_count = int(input_file.readline())  #number of test cases
    
    output_file = file("A-small-attempt0.out", "w")
    
    for test_case_counter in xrange(test_case_count):
        lines1 = (input_file.readline().replace('\n','')).split(' ')
        A = int(lines1[0])
        N = int(lines1[1])
        lines1 = (input_file.readline().replace('\n','')).split(' ')
        V1 = []
        for i in xrange(N):
          V1.append(int(lines1[i]))
        
        V1.sort()
        operations = 0
        #print A, N, V1
        
        mot_size = A
        for i in xrange(N):
            if mot_size > V1[i]:
                mot_size = mot_size + V1[i]
            else:
                if mot_size == 1:
                    operations = operations + N-i
                    break
                else:
                    opReq, temp_mot = findAddOperationReq(mot_size, V1[i])
                    #print opReq, temp_mot, N-i
                    if opReq < N-i:
                        operations = operations + opReq
                        mot_size = temp_mot + V1[i]
                    else:
                        operations = operations + N-i
                        break
        #print operations
        output_file.write("Case #"+str(test_case_counter+1)+": "+ str(operations)+"\n")
        

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("A-small-attempt1.in")
    prepare_input(input_file)
