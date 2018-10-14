import sys
from collections import defaultdict

def calculate_right(empty_stall, right):
    return right - empty_stall

def calculate_left(start, empty_stall):
    return empty_stall - start



def start_allocation(people, stalls):
    stall_min_max = defaultdict(list)
    for stall in range(0, stalls):
        stall_min_max[stall] = [calculate_left(0, stall), calculate_right(stall, stalls-1)]
    #print stall_min_max
    for person in range(0, people):
        cur_min = -1
        cur_max = -1
        for stall in stall_min_max:
            left = stall_min_max[stall][0]
            right = stall_min_max[stall][1]
            cur_stall = stall
            stall_min = min(left, right)
            stall_max = max(left, right)
            if((stall_min > cur_min) or (stall_min == cur_min and stall_max > cur_max)):
                cur_min = stall_min
                cur_max = stall_max
                the_stall = cur_stall
        #print "xx", the_stall, person
        stall_min_max[the_stall] = [-1, -1] # filled

        stall_count = 1
        while((the_stall - stall_count) >= 0):
            cur_stall = the_stall - stall_count
            left_stall = stall_min_max[cur_stall]
            #print left_stall
            if(left_stall[0] == -1): break
            left_stall[1] = the_stall - cur_stall - 1
            stall_count += 1
        stall_count = 1
        while((stall_count + the_stall) < stalls):
            cur_stall = the_stall + stall_count
            right_stall = stall_min_max[cur_stall]
            if(right_stall[0] == -1): break
            right_stall[0] = cur_stall - the_stall -1
            stall_count += 1
    return cur_max, cur_min
    #print stall_min_max

input_count = int(raw_input())
index = 1
while (input_count > 0):
    cur_line = raw_input().split()
    n = int(cur_line[0])
    k = int(cur_line[1])
    result = start_allocation(k,n)
    sys.stdout.write("Case #{}: {} {}\n".format(str(index), result[0], result[1]))
    input_count -= 1
    index += 1
