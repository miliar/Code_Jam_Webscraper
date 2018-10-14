
'''
3
---+-++- 3
+++++ 4
-+-+- 4
'''
with open("A-large.in") as input_file:
    input_rows = input_file.readlines()


num_rows = int(input_rows[0].replace('\n',''))
#print(num_rows)
del input_rows[0]

#print(input_rows)
test_cases = []
for i in input_rows:
    test_cases.append(i.replace('\n',''))


print(test_cases)





def find_flip_count(pancake_str,k):
    can_solve = True
    line_length = len(pancake_str)
    pan_list = [0]*line_length
    flip_count = 0
    
    for i in range(line_length):
        if pancake_str[i] == "+":
            pan_list[i] = 1
            
    for i in range(line_length-k+1):
        if pan_list[i] == 0:
            for j in range(k):
                pan_list[i+j] = 1 - pan_list[i+j]           
            flip_count += 1
            
    for i in range(line_length-k+1,line_length):
        if pan_list[i] == 0:
            can_solve = False
            break

    if can_solve == True:
        return flip_count
    else:
        return "IMPOSSIBLE"

case_num = 0
results = []
for i in test_cases:
    case_num += 1
    
    pancake_str = i[:i.find(" ")]

    k = int(i[i.find(" ")+1:])

    #print(find_flip_count(pancake_str,k))
    results.append('Case #' + str(case_num) + ': ' + str(find_flip_count(pancake_str,k)))

#print(results)

with open("output1_large.txt",'w') as output_file:
    
    for i in results:
        output_file.write("%s\n" % i)

