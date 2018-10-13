# X O O O O O O O X X O O X

# 0 1 2 3 4 5 6 7 8 9

# X O O O X

import sys
import pprint

input_array = [
        ['X'],
        [0,2],
        [1,1],
        [2,0],
        ['X'],
        [0,2],
        [1,1],
        [2,0],
        ['X'],
        ['X'],
        ['X'],
        [1,0],
        [0,1],
        ['X'],
]

def find_stall(array):
    mins = []
    max_min_val = float('-inf')

    for i in range(len(array)):
        if array[i][0] == 'X':
            continue
        cur_min = min(array[i])
        if cur_min > max_min_val:
            max_min_val = cur_min
            mins = [i]
        elif cur_min == max_min_val:
            mins.append(i)

    #print (mins)
    #print (max_min_val)
    if len(mins) == 1:
        return mins[0]

    #print ("Tie. Checking max. Mins are " + str(mins))
    maxs = []
    max_val = -1
    for i in range(len(mins)):
        array_i = mins[i]
        cur_max = max(array[array_i])

        if cur_max > max_val:
            maxs = [array_i]
            max_val = cur_max
        elif cur_max == max_val:
            maxs.append(array_i)

    if len(maxs) == 1:
        return maxs[0]
    else:
        return min(maxs)

        #print ("Tie. Maxs are" + str(maxs) + " Taking left: " + str(maxs))

def put_people(array_size, num_people):
    arr = ['X' for i in range(array_size)]
    for i in range(1, array_size - 1):
        arr[i] = [i - 1, array_size - 2 - i]

    #print (arr)

    for i in range(num_people):
        guy_at = find_stall(arr)

        guy_status = arr[guy_at]

        j = guy_at - 1
        while arr[j] != 'X':
            arr[j][1] -= guy_status[1] + 1
            j-= 1

        j = guy_at + 1
        while arr[j] != 'X':
            arr[j][0] -= guy_status[0] + 1
            j += 1
        arr[guy_at] = 'X'
        #print (arr)

    guy_status
    return guy_status



with open('q3_input.txt', 'r') as f:
    lines = f.readlines()
    num_cases = eval(lines[0])

    for i in range(1, len(lines)):
        splits = lines[i].split(' ')
        num_stalls = 2 + eval(splits[0])
        num_people = eval(splits[1])

        arr = put_people(num_stalls, num_people)
        print ("Case #" + str(i) + ": " + str(arr[1]) + ' ' + str(arr[0]))

#print (find_X(input_array))
