sample = open('B-large.in')
line = []
data = []
while sample:
    next_line = sample.readline()
    if next_line == "":
        break 
    else:
        line.append(next_line)
for num_set in line:
    new_set = num_set.rstrip().split(" ")
    int_set = []
    for nums in new_set:
        nums = int(nums)
        int_set.append(nums) 
    data.append(int_set)
    
print data

n_set= data[0]
n= n_set[0]

outfile = open('googledance.txt', 'w')

for number in xrange(1,n+1):
    case = data[number]
    n_case = case[0]
    s_case =case[1]
    p_case = case[2]
    contestants = case[3:]
    p_reach = 0
    s_reach = 0
    results = []
    ##now for the actual logic
    for contestant in contestants:
        ave_score = contestant/3
        remainder = contestant%3
        if remainder == 0 and ave_score >= p_case:
            p_reach += 1
        elif remainder == 0 and ave_score+1 >= p_case and ave_score>0:
            if s_reach < s_case:
                p_reach += 1
                s_reach += 1
        elif remainder == 1 and ave_score+1 >= p_case:
            p_reach += 1
        elif remainder == 2 and ave_score+1 >= p_case:
            p_reach += 1
        elif remainder == 2 and ave_score+2 >= p_case:
            if s_reach < s_case:
                p_reach += 1
                s_reach += 1
    outfile.write("Case #%d: %d\n" %(number, p_reach))
outfile.close()
        
        
            
        
        
    
