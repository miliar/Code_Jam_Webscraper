

with open("B-small-attempt0.in") as input_file:
    input_rows = input_file.readlines()


num_rows = int(input_rows[0].replace('\n',''))
#print(num_rows)
del input_rows[0]

#print(input_rows)
test_cases = []
for i in input_rows:
    test_cases.append(i.replace('\n',''))


#print(test_cases)


def is_tidy(N):
    #N a list
    if len(N) == 1:
        return True
    for i in range(len(N) - 1):
        if N[i] > N[i+1]:
            return False
    return True

def make_str(N):
    result = ''
    for i in N:
        result = result + str(i)
    return str(int(result))

def find_last_tidy(N):
    
    
    #teststr = '35789243'
    test_list = []
    for i in N:
        test_list.append(int(i))

    if is_tidy(test_list) == True:
        return N
        
    lastindex = len(N) - 1
    for i in range(lastindex):
        if test_list[i] >= test_list[i+1]:
            test_list[i] = test_list[i] - 1
            for j in range(i+1,lastindex+1):
                test_list[j] = 9
            break

    return make_str(test_list)

case_num = 0
results = []    
for i in test_cases:
    case_num += 1
    #results.append(find_last_tidy(i))
    #print(find_last_tidy(i))
    results.append('Case #' + str(case_num) + ': ' + str(find_last_tidy(i)))

with open("output2_small.txt",'w') as output_file:
    
    for i in results:
        output_file.write("%s\n" % i)

