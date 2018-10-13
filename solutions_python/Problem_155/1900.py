import sys
case_number = 1
tot = 0
guest = 0
with open(sys.argv[1], 'r') as fp:
    for line in fp:
        if(len(line.split(' ')) == 1):
            continue
        print('Case #{0}: '.format(case_number), end='')  
        (max_shy, shy) = line.split(' ')
        for i in range(0, int(max_shy) + 1):
            tot = tot + int(shy[i])
            if (tot <= i):
                guest = guest + 1    
                tot = tot + 1        
        print(guest)        
        tot = 0
        guest = 0    
        case_number = case_number + 1
