from IO import *

input_file_name = get_input_file_name()
# input_file_name = 'test input'
# input_file_name = 'A-small-practice.in'
# input_file_name = 'A-large-practice.in'
print input_file_name
file_contents = read_input(input_file_name, ['T'], ['NK'], try_cast=True)

num_cases = file_contents[0]['T']
case_inputs = file_contents[1]

outputs = []

def pick_stall(stalls):

    for l in range(1, len(stalls)+2):
        if stalls.find(l * '0') == -1:
            break

    l -= 1
    i = stalls.find(l * '0')

    stalls = list(stalls)

    if l % 2 != 0:
        stalls[i + l / 2] = '1'
    else:
        stalls[i + - 1 + l / 2] = '1'

    stalls = ''.join(stalls)
    # print l, i, stalls
    return stalls

for inputs in case_inputs:

    n = int(inputs['NK'].split(' ')[0])
    k = int(inputs['NK'].split(' ')[1])

    print n, k

    stalls = '0' * n

    for _ in xrange(k-1):
        stalls = pick_stall(stalls)

    print stalls

    for l in range(1, len(stalls) + 2):
        if stalls.find(l * '0') == -1:
            break

    l -= 1

    max = l / 2
    min = (l - 1) / 2

    print max, min
    outputs.append([max, min])

    print ''


write_list_of_lists(outputs)
