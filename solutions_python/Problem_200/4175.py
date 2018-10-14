def get_descending_index(digit_list):
    d_index = -1 # descending index
    for i, digit in enumerate(digit_list):
        if i < len(digit_list) - 1:
            if int(digit_list[i]) > int(digit_list[i + 1]):
                return i
    return d_index

def find_stop_index(digit_list, d_index, threshold):
    for i in range(d_index - 1, -1, -1):
        if threshold < digit_list[i]:
            pass
        else:
            return i
    return 0

def process_back(digit_list, d_index):
    if d_index < 0:
        return digit_list

    digit_list[d_index] = digit_list[d_index] - 1
    threshold = digit_list[d_index]

    for i in range(d_index + 1, len(digit_list)): digit_list[i] = 9
    stop_index = find_stop_index(digit_list, d_index, threshold)

    if stop_index >= 0:
        # if stop_index == 0:
        #     digit_list[stop_index] = digit_list[stop_index] - 1
        # print digit_list
        # print stop_index, d_index
        if stop_index == d_index - 1:
            # for i in range(d_index + 1, len(digit_list)): digit_list[i] = 9
            pass
            # digit_list[stop_index] = digit_list[stop_index] - 1

        else:
            if stop_index != d_index:
                digit_list[stop_index] = digit_list[stop_index] - 1
            for i in range(stop_index + 1, len(digit_list)): digit_list[i] = 9
        # print digit_list
        # print stop_index, d_index
        # if stop_index == 0:
        #     digit_list[stop_index] = digit_list[stop_index] - 1
        #     for i in range(stop_index, len(digit_list)): digit_list[i] = 9
        # print digit_list[i],
        # print ''
    if digit_list[0] > digit_list[1]:
        digit_list[0] = digit_list[0] - 1
        for i in range(1, len(digit_list)): digit_list[i] = 9
    # else:
    #     digit_list[stop_index] = digit_list[stop_index] - 1
    #     for i in range(stop_index, len(digit_list)): digit_list[i] = 9
    return digit_list

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    number_string = raw_input()
    digit_list = [int(digit) for digit in number_string]
    answer = 0
    d_index = get_descending_index(digit_list)
    # print ''
    processed_list = process_back(digit_list, d_index)
    answer = ''
    for d in processed_list:
        if d > 0: answer = '{}{}'.format(answer, d)
    print "Case #{}: {}".format(i, answer)

'''
Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999
Case #5: 56669
Case #6: 59999
Case #6: 899
'''
