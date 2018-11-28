import math
import bisect

def osmos():
    """
        used to solve google code jam 2013 Round 1B - Problem A
    """
    in_f = open('A-small-attempt0.in', 'r')
    out_f = open('output.txt', 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
#    print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)
        
def solve_case(in_f, out_f, case_index):
    """
    solve each case
    """
    print "start handling case #{}".format(case_index)
    #
    bound_info = in_f.readline().rstrip('\n').split(" ")
    init = int(bound_info[0])
    N = int(bound_info[1])
    print("{} {}".format(init, N))
    
    line = in_f.readline().rstrip('\n')
    num_list = line.split(" ")
    for x in xrange(0, N):
        num_list[x] = int(num_list[x])
    print num_list
    num_list.sort()
    print num_list
    min_steps = get_min_steps(0, init, num_list)
    out_f.write("Case #{}: {}\n".format(case_index, min_steps))

def get_min_steps(current_steps, current_size, remaining_list):
    print "{} {} {}".format(current_steps, current_size, remaining_list)
    length = len(remaining_list)
    re_list = remaining_list
    temp_current_size = current_size
    for x in xrange(0, length):
        if temp_current_size > re_list[0]:
            temp_current_size = temp_current_size + re_list.pop(0)
    if len(re_list) == 0:
        return current_steps

    # test if there are two options available
    smaller_num = temp_current_size-1
    if smaller_num == 0:
        o0_re_list = list(re_list)
        o0_re_list.pop(0)
        return get_min_steps(current_steps + 1, temp_current_size, o0_re_list)
    else:
        # add a number
        o1_re_list = list(re_list)
        o1_re_list.insert(0, smaller_num)
        option_1_steps = get_min_steps(current_steps + 1, temp_current_size, o1_re_list)
        # remove a number
        o2_re_list = list(re_list)
        o2_re_list.pop(0)
        option_2_steps = get_min_steps(current_steps + 1, temp_current_size, o2_re_list)
        return min(option_1_steps, option_2_steps)
    
if __name__ == '__main__':    
    osmos()

