#!/usr/bin/env python2.7
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def checkBlankCount(string_list):
    """
    :input: list of char
    """
    count = 0
    length = len(string_list)
    for x in xrange(length):
        if string_list[x] != '+':
            count = count + 1
    return count

def returnTheOtherSign(sign):
    """
    :input: char
    """
    if sign == '+':
        return '-'
    else:
        return '+'


def doFlip(string_list, k_size, flip_position):
    #print "flip"
    #print string_list
    length = len(string_list)
    return_str = []
    flip_end_position = (flip_position + k_size - 1) 
    #print str(flip_end_position) + " " + str(length) +" "+str(flip_position)+ " " + str(k_size) 
    if flip_end_position >= length:
        return string_list

    return_str[:] = string_list[:]
    for x in xrange(flip_position, flip_end_position+1):
        return_str[x] = returnTheOtherSign(string_list[x])
    #print return_str
    #print "flip end"
    return return_str
    #return string_list


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s, k = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    k_size = int(k)
    length = len(s)
    queue_list = []
    queue_list.append(list(s))

    impossible_flag = 0 
    end_check_point = (length - k_size) 
    start_check_point = (k_size-1)
    check_length = start_check_point - end_check_point
    if end_check_point < start_check_point:
        for x in xrange(end_check_point, start_check_point):
            if checkBlankCount(queue_list[0][end_check_point:start_check_point]) != 0:
                if checkBlankCount(queue_list[0][end_check_point:start_check_point]) != check_length:
                    print "Case #{}: IMPOSSIBLE".format(i)
                    impossible_flag = 1
                    break
    #print queue_list
    if impossible_flag == 1:
        continue

    steps = 0
    blank_count = checkBlankCount(queue_list[0])
    while blank_count != 0:
        steps = steps + 1
        original_str = queue_list[0]
        for x in xrange(length):
            #def doFlip(string_list, k_size, flip_position):
            if queue_list[0][x] == '-':
                temp_str = doFlip(queue_list[0], k_size, x)
                #print temp_str
                #print original_str
                if temp_str == original_str:
                    impossible_flag = 1
                queue_list.append(temp_str)
                break
        del queue_list[0]
        blank_count = checkBlankCount(queue_list[0])
        if queue_list[0] == list(s) or impossible_flag == 1:
            print "Case #{}: IMPOSSIBLE".format(i)
            impossible_flag = 1
            break
            
        #print queue_list

    if impossible_flag == 1:
        continue
    #print queue_list
    # "IMPOSSIBLE"
    print "Case #{}: {}".format(i, steps)
    #print "Case #{}: {}".format(i, final_result)
    # check out .format's specification for more formatting options
