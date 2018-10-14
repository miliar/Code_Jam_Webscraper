# -*- coding: utf-8 -*-
import sys

def offset_digit(len_num):
    if len_num == 1:
        return 0
    elif len_num == 2:
        return 10
    else:
        half = (len_num-1)/2
        remain = len_num-1-half
        return offset_digit(len_num-1) + 10**(half)-1 + 1 + 10**(remain)-1

def minimum_count(num):
    str_num = str(num)
    len_num = len(str_num)

    if len_num == 1:
        return num

    half = (len_num)/2
    remain = len_num-half
    #print str_num
    #print str_num[:half]
    #print int(str_num[-remain:])
        
    if sum(map(int, str_num[:half])) == 1:
        return num - 10**(len_num-1) + offset_digit(len_num)

    elif int(str_num[-remain:]) == 0:
        return 1 + minimum_count(num-1)

    return int(str_num[-remain:]) + int(str_num[:half][::-1]) + offset_digit(len_num)

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    test_num = int(f.readline())

    for i in xrange(1, test_num+1):
        data = int(f.readline())
        ans = minimum_count(data)
        print('Case #%i: %s' % (i, ans) )
