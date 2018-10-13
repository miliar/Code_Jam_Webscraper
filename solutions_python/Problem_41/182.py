'''
Created on Sep 13, 2009

@author: Aaron
'''

import sys
sys.stdin = file("B-small.in")

num_cases = 0

def all_digits_present_in_number(digits, number):
    for _index in range(len(number)):
        if number[_index] not in digits:
            return False
        digits.remove(number[_index])
    return True

if __name__ == '__main__':
    num_cases = int(sys.stdin.next().strip())
    for _index in range(num_cases):
        _str_num = sys.stdin.next().strip()
        _num = int(_str_num) + 1
        while not all_digits_present_in_number(list(_str_num), str(_num)):
            _num += 1
            if (len(str(_num)) > len(_str_num)):
                _str_num += '0'
        print 'Case #%d: %d' % (_index + 1, _num)