import math

t = int(raw_input().strip())
for ti in range(1, t+1):
    n, k = [int(x) for x in raw_input().strip().split(' ')]
    stall_arr = [n]
    
    for ki in range(k):
        new_n = stall_arr[0] - 1
        left = math.floor(new_n/2.0)
        right = math.ceil(new_n/2.0)
        del stall_arr[0]
        stall_arr.append(left)
        stall_arr.append(right)
        stall_arr.sort(reverse=True)
    
    maxLR = int(max([left, right]))
    minLR = int(min([left, right]))
    
    print 'Case #' + str(ti) + ': ' + str(maxLR) + ' ' + str(minLR)