for T in range(1, int(raw_input()) + 1):
    minLR = 0
    maxLR = 0
    
    stall_num, people = map(int,(raw_input().split()))
    stalls = [stall_num] 
    
    i=0
    
    while i < people:
        
        stall_seq = max(stalls)
        index = stalls.index(stall_seq) 
        
        if stall_seq%2 == 1:
            minLR = stall_seq//2
            maxLR = stall_seq - minLR - 1
        else:
            minLR = stall_seq//2 - 1
            maxLR = stall_seq - minLR - 1 
            
        if minLR == 0:
            stalls = stalls[:index] + [maxLR] + stalls[index + 1:]
        elif maxLR == 0:
            stalls = stalls[:index] + [minLR] + stalls[index + 1:]
        else:
            stalls = stalls[:index] + [minLR] + [maxLR] + stalls[index + 1:] 
            
        i += 1
        
    print('Case #'+str(T)+': '+ str(maxLR) + ' '+ str(minLR))