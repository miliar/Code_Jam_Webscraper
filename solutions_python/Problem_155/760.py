def opera(case_list):
    
    sat = []
    for e in case_list:
        sat.append(int(e))
    
    t = sum(sat)
    standing = sat[0]
    invites = 0
    
    s_list = []
    count = 0
    for i in sat:
        if i > 0:
            s_list.append(count)
        count += 1
    if s_list[0] == 0:
        s_list = s_list[1:]
    
    while standing < t:
        for i in s_list:
            if standing >= i:
                standing += sat[i]
            else:
                while standing < i:
                    standing += 1
                    invites += 1
                standing += sat[i]
    
    return invites


input_file = open('C:\Users\chrisjwaite\Desktop\\A-large.in')
output_file = open('C:\Users\chrisjwaite\Desktop\\A-large_output.out', 'w')
lines = input_file.read().split('\n')

n_cases = int(lines[0])
case_list = []

for case in lines[1:-1]:
    data = case.split(' ')
    case_list.append(data[1])

for i in range(n_cases):
    output_file.write('Case #' + str(i+1) + ': ' + str(opera(case_list[i])) + '\n')

input_file.close()
output_file.close()

    
    
