from itertools import *

test_cases = int(raw_input())


def is_tidy(num):
    return num == int(''.join(sorted(str(num))))


def get_tidy(number):
    # if its already tidy, just return it
    if len(str(number)) == 1 or is_tidy(number):
        return number

    to_deduct = 0
    tidy_number = number

    digits_list = [int(d) for d in str(number)]
    number_len = len(digits_list)

    for index in reversed(range(1, number_len)):
        if index + 1 == number_len:
            # print (' '*(index-1)) + '-' + str(digits_list[index] + 1)
            
            to_deduct += digits_list[index] + 1
            tidy_number = number - int(digits_list[index] + 1)
        
        elif digits_list[index] == 0:
            continue
        else:
            # print (' '*(index-1)) + '-' + str(digits_list[index]) + str('0'*(number_len-index-1))
            
            tidy_number = number - int(str(digits_list[index]) + str('0'*(number_len-index-1)))
            to_deduct += int(str(digits_list[index]) + str('0'*(number_len-index-1)))

        # print tidy_number
        if is_tidy(tidy_number):
            return tidy_number

    return number - to_deduct


for case in xrange(1, test_cases + 1):
    number = [int(n) for n in raw_input().split(" ")]
    print "Case #{}: {}".format(case, get_tidy(number[0]))
