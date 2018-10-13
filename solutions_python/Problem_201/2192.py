

with open("C-small-2-attempt0.in") as input_file:
    input_rows = input_file.readlines()


num_rows = int(input_rows[0].replace('\n',''))
#print(num_rows)
del input_rows[0]

#print(input_rows)
test_cases = []
for i in input_rows:
    test_cases.append(i.replace('\n',''))


#print(test_cases)





#N = 4
#S = 2

def find_prev_power_2(S):
    count = 0
    rem = S
    while rem >= 2:
        count += 1
        rem = rem/2.0
    return count

def find_max_min_gaps(test_string):

    N = int(test_string[:test_string.find(' ')])
    S = int(test_string[test_string.find(' ')+1:])
    
    num_placed = (2 ** find_prev_power_2(S)) - 1

    space_size = (N-(num_placed))/float(num_placed + 1)

    small_space_size = int(space_size)
    if space_size - small_space_size == 0:
        num_large_space = 0
    elif small_space_size == 0:
        num_large_space = (num_placed + 1)*(space_size - small_space_size)
    #elif small_space_size == 1:
    #    num_large_space = N - num_placed - num_placed - 1
    else:
        num_large_space = (N-num_placed) - (small_space_size * (num_placed + 1))

    num_left_to_place = S - num_placed

    if num_left_to_place <= num_large_space:
        current_gap = small_space_size + 1
    else:
        current_gap = small_space_size

    max_gap = int(current_gap/2.0)
    min_gap = int((current_gap - 1)/2.0)

    return [max_gap, min_gap]



case_num = 0
results = []    
for i in test_cases:
    case_num += 1
    interim_result = find_max_min_gaps(i)
    #results.append(find_max_min_gaps(i))
    #print(find_max_min_gaps(i))
    results.append('Case #' + str(case_num) + ': ' + str(interim_result[0]) + ' ' + str(interim_result[1]))

#print(results)

with open("output3_small_2.txt",'w') as output_file:
    
    for i in results:
        output_file.write("%s\n" % i)


