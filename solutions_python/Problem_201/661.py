
'''
Code Jam 2017
Problem C. Bathroom Stalls
'''
T = int(input())  # read a line with a single integer
def find_distance(stall, hooman):
    '''
    do some math
    '''
    #init val
    max_distance = stall // 2
    min_distance = (stall - 1) // 2
    stack = {}
    keys = []
    stack[max_distance] = 1
    keys.append(max_distance)
    if min_distance == max_distance:
        stack[min_distance] += 1
    else:
        stack[min_distance] = 1
        keys.append(min_distance)
    hooman -= 1
    while hooman > 0:
        stalls = keys[0]
        delta = stack[stalls]
        if stalls == 1:
            return 0, 0
        hooman = hooman - delta
        stack.pop(stalls)
        del keys[0]
        max_distance = stalls // 2
        min_distance = (stalls - 1)//2
        if max_distance in keys:
            stack[max_distance] += delta
        else:
            stack[max_distance] = delta
            keys.append(max_distance)
        if min_distance in keys:
            stack[min_distance] += delta
        else:
            stack[min_distance] = delta
            keys.append(min_distance)
    return max_distance, min_distance
for i in range(1, T + 1):
    test, count = [int(s) for s in input().split(" ")]
    max_dis, min_dis = find_distance(test, count)
    print("Case #{}: {} {}".format(i, max_dis, min_dis))
