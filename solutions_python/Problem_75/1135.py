import sys
from collections import deque

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline().strip('\n'))
num_cases += 1

for c in range(1, num_cases):
    can_combine = dict()
    combine = dict()
    are_oposed = dict()
    previous = []
    
    case = 'Case #' + str(c) + ': '
    case_info = in_file.readline().strip('\n').split(' ')

    com = int(case_info[0]) + 1

    for combination in range(1, com):
        can_combine[case_info[combination][0]] = case_info[combination][1]
        can_combine[case_info[combination][1]] = case_info[combination][0]

        combine[case_info[combination][0]] = case_info[combination][2]
        combine[case_info[combination][1]] = case_info[combination][2]

    op = com + 1
    op_fin = op + int(case_info[com])

    for oposition in range(op, op_fin):
        are_oposed[case_info[oposition][0]] = case_info[oposition][1]
        are_oposed[case_info[oposition][1]] = case_info[oposition][0]

    invocation_len = int(case_info[op_fin])
    invocation = case_info[op_fin + 1]
    result = deque()
    read = set(result)
    result_last = -1

    for x in range(0, invocation_len):
        if result:
            result.append(invocation[x])
            result_last += 1
            read = set(result)

            if (can_combine.has_key(result[result_last])):
                if (can_combine[result[result_last]] == result[result_last - 1]):
                    z = result.pop()
                    result_last -= 1
                    result.pop()
                    result_last -= 1
                    
                    result.append(combine[z])
                    result_last += 1
                else:
                    if (are_oposed.has_key(result[result_last])):
                        if (are_oposed[result[result_last]] in read):
                            result = deque()
                            result_last = -1
            else:
                if (are_oposed.has_key(result[result_last])):
                    if (are_oposed[result[result_last]] in read):
                        result = deque()
                        result_last = -1
        else:
            result.append(invocation[x])
            result_last += 1
            read = set(result)

    out_file.write(case + '[' + (', ').join(list(result)) + ']\n')
