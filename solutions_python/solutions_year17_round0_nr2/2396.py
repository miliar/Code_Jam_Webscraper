import numpy as np

## n test cases
cases = int(input())

for case in range(cases):
    ## case inputs
    num = np.array(list(input()), np.int8)
    num_len = len(num)
    pos_sentinel = 0
    pos_prev = 0

    ## find sentinel
    for pos_current in range(1, num_len):
        if (num[pos_current] < num[pos_current-1]):
            break
        elif (num[pos_current] != num[pos_sentinel]):
            pos_sentinel = pos_current
        pos_prev = pos_current

    ## just break if correct
    if (pos_prev+1 == num_len):
        num = ''.join(num.astype('str'))
        print('Case #' + str(case + 1) + ':', str(int(num)))
        continue

    ## pad with 9's
    if num_len > 0:
        num[pos_sentinel+1:] = 9

    ## find greatest before sentinel
    num[pos_sentinel] -= 1

    ## output
    num = ''.join(num.astype('str'))
    print('Case #' + str(case + 1) + ':', str(int(num)))
