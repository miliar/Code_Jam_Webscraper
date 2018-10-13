def pancake(stack_str):
    
    str_list = stack_str.split(' ')
    stack_list = []
    for e in str_list:
        stack_list.append(int(e))
    
    
    P_max = max(stack_list)
    
    best_time = P_max
    
    for i in range(1, P_max):
        minutes = i
        
        for s in stack_list:
            while s > i:
                s = s - i
                minutes += 1
        
        if minutes < best_time:
            best_time = minutes
    
    return best_time
    


input_file = open('C:\Users\chrisjwaite\Desktop\\B-large.in')
output_file = open('C:\Users\chrisjwaite\Desktop\\B-large.out', 'w')
lines = input_file.read().split('\n')
n_cases = int(lines[0])
case_list = []
lines = lines[1:]
r = range(1, len(lines), 2)
for i in r:
    case_list.append(lines[i])
for i in range(n_cases):
    answer = pancake(case_list[i])
    output_file.write('Case #' + str(i+1) + ': ' + str(answer) + '\n')
input_file.close()
output_file.close()