case_prefix = 'Case #'

def build_result_string(case_num, verdict):
    return case_prefix + str(case_num) + ': ' + verdict

def determine_result(case_num, num_snappers, num_snaps):
    two_to_n = 1 << num_snappers
    num_snaps_plus_one = num_snaps + 1
    if num_snaps_plus_one < two_to_n:
        print build_result_string(case_num, 'OFF')
        return
    if num_snaps_plus_one == two_to_n:
        print build_result_string(case_num, 'ON')
        return
    if num_snaps_plus_one & (two_to_n - 1) == 0:
        print build_result_string(case_num, 'ON')
    else:
        print build_result_string(case_num, 'OFF')
        

f = open('A-large.in', 'r')
num_tests = int(f.readline().strip())

for case in range(num_tests):
    (num_snappers, num_snaps) = (long(t) for t in f.readline().strip().split())                                
    determine_result(case + 1, num_snappers, num_snaps)
                                 
