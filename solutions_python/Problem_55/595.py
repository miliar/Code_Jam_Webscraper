case_prefix = 'Case #'

def build_result_string(case_num, verdict):
    return case_prefix + str(case_num) + ': ' + verdict

def increment(pos, max_size):
    return (pos + 1) % max_size

def determine_result(case_num, num_times, capacity, groups):
    num_groups = len(groups)
    ptr = 0
    earnings = 0
    if num_groups == 0 or capacity == 0 or num_times == 0:
        print build_result_string(case_num, str(earnings))
        return

    if num_groups == 1:
        if groups[0] <= capacity:
            earnings = num_times * groups[0]
            print build_result_string(case_num, str(earnings))
            return
        else:
            print build_result_string(case_num, str(earnings))
            return

    sum_of_groups = sum(groups)
    if sum_of_groups <= capacity:
        earnings = num_times * sum_of_groups
        print build_result_string(case_num, str(earnings))
        return

    for time in range(num_times):
        used_capacity = 0
        remaining_capacity = capacity
        first_group_in_coaster = None
        while True:
            if ptr == first_group_in_coaster:
                break
            group_size = groups[ptr]
            if group_size <= remaining_capacity:
                if first_group_in_coaster == None:
                    first_group_in_coaster = ptr
                remaining_capacity = remaining_capacity - group_size
                used_capacity = used_capacity + group_size
                ptr = increment(ptr, num_groups)
            else:
                break
        earnings = earnings + used_capacity
        
    print build_result_string(case_num, str(earnings))

f = open('C-small-attempt1.in', 'r')
num_tests = int(f.readline().strip())

for case in range(num_tests):
    (num_times, capacity, num_groups) = (long(t) for t in f.readline().strip().split())
    groups = [long(t.strip()) for t in f.readline().strip().split()]
    determine_result(case + 1, num_times, capacity, groups)
