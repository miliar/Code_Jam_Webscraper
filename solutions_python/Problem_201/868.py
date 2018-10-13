#stalls v2

def decimal_to_binary(base10):
    base2 = []
    while base10 != 0:
        base2.append(1 if base10%2 > 0.5 else 0) 
        base10 = base10 // 2
    base2.reverse()
    return base2

t = int(input())
for i in range(1,t+1):
    constants = input().split()
    N = int(constants[0])
    K = int(constants[1])
    
    #calculate K in binary
    K_binary = decimal_to_binary(K)
    
    #calculate p
    p = len(K_binary)-1
    
    #find split number
    #splits = K_binary[1:len(K_binary)]
    
    #iterate through splits to reach n before last split
    n = N
    
    '''
    for s in range(0,len(splits)):
        smallest = (n-1)//2
        largest = (n-1) - smallest        
        if splits[s] == 0:
            n = largest
        else:
            n = smallest
    #last split gives min and max
    n = 1 if n == 0 else n
    smallest = (n-1)//2
    largest = (n-1) - smallest    
    print("Case #{}: {} {}".format(i,largest,smallest))
    
    '''

    min_gap = N
    max_gap = N
    n_min = 1
    n_max = 0
    
    for s in range(0,p):
        if min_gap % 2 > 0.5:
            n_min = 2 * n_min + n_max
        else:
            n_max = 2 * n_max + n_min
        min_gap = (min_gap-1)//2
        max_gap = (max_gap)//2
        #print("split {}: {}({}),{}({})".format(s,min_gap,n_min,max_gap,n_max))

    leftover = K - (pow(2,p) - 1)
    smallest = 0
    largest = 0
    if leftover <= n_max:
        smallest = (max_gap-1 )//2
        largest = (max_gap-1) - smallest
    else:
        smallest = (min_gap-1 )//2
        largest = (min_gap-1) - smallest
    print("Case #{}: {} {}".format(i,largest,smallest))
    '''
    
    people_moved = 0
    iteration = 0
    n = N
    
    final_min = 0
    final_max = 0
    
    while True:
        smallest = (n-1)//2
        largest = (n-1) - smallest
        people_moved += pow(2,iteration)
        iteration += 1
        if people_moved >= K:
            final_min = smallest
            final_max = largest
            break
        else:
            n = largest
    
    print("Case #{}: {} {}".format(i,final_max,final_min))
    '''