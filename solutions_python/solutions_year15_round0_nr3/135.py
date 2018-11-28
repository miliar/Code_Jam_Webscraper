# -*- coding: utf-8 -*-
import sys
int_ijk = [2,3,4]

def ijk_to_int(char):
    return ord(char) - ord('i') + 2

def calc(elem1, elem2):
    abs1 = abs(elem1)
    abs2 = abs(elem2)
    sign = (elem1 * elem2) / (abs1 * abs2)

    if abs1 == 1 or abs2 == 1:
        return elem1 * elem2

    elif abs1 == abs2:
        return -1 * sign

    else:
        if (abs2 - abs1) % 3 == 2:
            sign *= -1
        return sign * (sum(int_ijk) - (abs1 + abs2))
    

def check_ijk(char_num, times, repeat_str):
    no = 'NO'
    yes = 'YES'

    if  1 == (('i' in repeat_str) + ('j' in repeat_str) + ('k' in repeat_str)):
        return no

    int_string = map(ijk_to_int, repeat_str)
    repeat_ans = 1
    for elem in int_string:
        repeat_ans = calc(repeat_ans, elem)

    if repeat_ans == 1 or repeat_ans == -1 and times % 2 == 0 or\
       abs(repeat_ans) != 1 and times % 4 != 2:
        return no
    
    next_search = 2
    ans = 1
    count = 0
    while count < times:
        for elem in int_string:
            ans = calc(ans, elem)
            if abs(ans) == next_search:
                if next_search == 3:
                    return yes
                next_search = 3
                ans /= abs(ans)
        count += 1
    
    return no

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    test_num = int(f.readline())

    for i in xrange(1, test_num+1):
        data = f.readline().split()
        repeat_str = f.readline()
        ans = check_ijk(int(data[0]), int(data[1]), repeat_str[:-1])
        print('Case #%i: %s' % (i, ans) )
