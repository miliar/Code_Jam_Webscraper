
import sys
import math

def left_distance(stalls,stall_index):
    distance = 0;
    for i in reversed(range(0,stall_index)):
        if stalls[i] == 1:
            return distance
        distance = distance +1
    return distance

def right_distance(stalls,stall_index):
    distance = 0;
    for i in range(stall_index+1,len(stalls)):
        if stalls[i] == 1:
            return distance
        distance = distance +1
    return distance

# returns max(l_d,r_d), min(l_d,r_d)
def compute_distances(stalls):
    max_left_distance = 0
    min_left_distance = len(stalls)-1
    max_right_distance = 0
    min_right_distance = len(stalls) - 1
    for i in range(1,len(stalls)-1):
        left_d = left_distance(stalls,i)
        right_d = right_distance(stalls,i)
        if left_d > max_left_distance:
            max_left_distance = left_d
        if left_d < min_left_distance:
            min_left_distance = left_d
        if right_d > max_right_distance:
            max_right_distance = right_d
        if right_d > min_right_distance:
            min_right_distance = right_d

    #print (max(max_left_distance,max_right_distance), min(min_left_distance,min_right_distance))
    return max(max_left_distance,max_right_distance), min(min_left_distance,min_right_distance)


def find_d_for_last_occupant_iterative(stalls, num_occupants):
    max_d = 0
    min_d = math.floor(len(stalls) / 2)
    indices = [k for k in range(1,len(stalls)-1)]
    for i in range (0, num_occupants):
        # compute d
        closest = 0
        closest_max = 0
        index = min(indices)
        for j in indices:
            if stalls[j] != 1:
                right = right_distance(stalls,j)
                left = left_distance(stalls,j)
                # closest = min(left,right)
                if min(left,right) > closest:
                    closest = min(left,right)
                    closest_max = max(left, right)
                    index = j
                if min(left,right) == closest:
                    if max(left,right) > closest_max:
                        closest_max =max(left,right)
                        closest = min(left,right)
                        index = j

        stalls[index] = 1
        indices.remove(index)
        max_d = closest_max
        min_d = closest
    return max_d,min_d


def find_d_for_last_occupant_split(stalls, num_occupants):
    if num_occupants == 1:
        if len(stalls) == 2:
            return 0,0
        if len(stalls) == 3:
            return 0,0
        if len(stalls) == 4:
            #shouldn't happen with num_occupants > 1
            return 1,0
        if len(stalls) == 5:
            #shouldn't happen with num_occupants > 1
            return 1,1
        left_stall_split = int(math.ceil(len(stalls) / 2))
        stalls[left_stall_split] = 1
        #print stalls
        return compute_distances(stalls)

    left_stall_split = int(math.ceil(len(stalls)/2))
    right_stall_split = int(math.floor(len(stalls)/ 2))
    left_occupants = int(math.ceil(num_occupants/2))
    right_occupants = int(math.floor(num_occupants/2))
    stalls[left_stall_split] = 1
    left_stalls = stalls[0:left_stall_split]
    right_stalls = stalls[right_stall_split:len(stalls)]
    left_stalls_max, left_min = find_d_for_last_occupant_split(left_stalls, left_occupants)
    right_stalls_max, right_min = find_d_for_last_occupant_split(right_stalls, right_occupants)
    return max(left_stalls_max,right_stalls_max), min(left_min,right_min)


def initialize_stalls(num_stalls):
    #print type(num_stalls)
    stalls = [0 for i in range(0,num_stalls+2)]
    stalls[0] = 1
    stalls [num_stalls+1] = 1
    return stalls

def bathroom_stalls(num_stalls, num_occupants):
    if num_stalls == num_occupants:
        return 0,0
    if 1.5*num_occupants > num_stalls:
        return 0,0
    stalls = initialize_stalls(num_stalls)
    #print(stalls)
    return find_d_for_last_occupant_iterative(stalls,num_occupants)


arg_list = sys.argv
input_file = open(arg_list[1])
output = open(arg_list[2], 'w')
j = 0
for line in input_file:
    if j ==0:
        num_cases = line
        j = j+1
    else:
        num_stalls,num_occupants = line.replace('\n', '').split(" ")
        print("input: " + str(j) + " : " + str(num_stalls) + " " +  str(num_occupants))
        max_d, min_d = bathroom_stalls(int(num_stalls),int(num_occupants))
        print("Case #{}: {} {}".format(j,max_d,min_d))
        output.write("Case #{}: {} {}\n".format(j, max_d,min_d))
        j = j + 1
