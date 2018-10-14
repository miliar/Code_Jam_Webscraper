def restroom_stall(stalls, people):
    level = people.bit_length() - 1
    
    max_stalls = stalls >> level
    
    mask = (1 << level) - 1
    
    wide_stalls_count = (stalls & mask) + 1

    maxLR = max_stalls >> 1
    minLR = maxLR - 1
    people_level = people - mask
    if people_level > wide_stalls_count:
        if max_stalls & 1 == 0 :
            maxLR -= 1
    else:
        if max_stalls & 1 == 1 :
            minLR += 1
        
        
    return maxLR, minLR



t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    maxlr, minlr = restroom_stall(n,k)
    print("Case #{}: {} {}".format(i,maxlr,minlr))
