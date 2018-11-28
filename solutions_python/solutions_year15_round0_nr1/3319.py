import sys

infile = open('A-large.in', 'r')

case_no = 0

for line in infile:
    
    case_no = case_no + 1
    
    components = line.split()
    s_max = int(components[0])
    shy_string = components[1]
    
    friends = 0
    total_sum = 0
        
    for i in range(s_max + 1):
        total_sum = total_sum + int(shy_string[i])
        if(total_sum < (i + 1)):
            friends = friends + 1
            total_sum = total_sum + 1
    
    print("Case #" + str(case_no) + ": " + str(friends))