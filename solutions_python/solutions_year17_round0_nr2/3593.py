import sys
import numpy as np # from https://github.com/numpy/numpy

def is_tidy(num):
    str_num = str(num)
    if len(str_num) == 1:
        return True
    old_ch = str_num[0]
    for ch in str_num[1:]:
        if int(ch) < int(old_ch):
            return False
        old_ch = ch
    return True

def is_tidy_improv(num):
    str_num = str(num)
    tidy = True
    if len(str_num) == 1:
        return tidy, num

    digits = np.ones((10)).astype(np.int32) * (len(str_num) - 1)
    digits2 = np.ones((10)).astype(np.int32) * -1
    old_ch = str_num[0]
    digits[int(old_ch)] = 0
    untidy_num = 0

    id1 = id2 = 0
    for i, ch in enumerate(str_num[1:]):
        digits[int(ch)] = np.minimum(digits[int(ch)], int(ch))
        digits2[int(ch)] = np.maximum(digits2[int(ch)], int(ch))
        if int(ch) < int(old_ch):
            tidy = False
            untidy_num = int(ch)
            id1 = i
            id2 = i + 1
        old_ch = ch

    if tidy:
        return tidy, num
    #untidy_num_2 = np.min(digits[untidy_num + 1:])
    #next_num = np.maximum(long('9' * (len(str_num) - 1)), num - 10 ** (len(str_num) - 1 - untidy_num_2))

    proposals = [long('9' * (len(str_num) - 1)), num - 10 ** (len(str_num) - id2 - 1)]
    prop = long('%s%s' % (str_num[:id2] , '0' * (len(str_num) - id2)))
    if prop < num:
        proposals.append(prop)
    prop = long('%s%s' % (long(str_num[:id2]) - 1, '9' * (len(str_num) - id2)))
    if prop < num:
        proposals.append(prop)
    #print proposals
    next_num = np.max(proposals)
    return [tidy, next_num]

num_cases = int(sys.stdin.readline().strip())

for i in range(num_cases):
    num = long(sys.stdin.readline().strip())

    tidy = False
    while not tidy:
        tidy, num = is_tidy_improv(num)
    #while not is_tidy(num):
    #    num -= 1
    print('Case #%d: %d' % (i+1, num))
