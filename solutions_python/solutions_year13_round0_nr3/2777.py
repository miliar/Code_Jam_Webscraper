__author__ = 'louyang'
import math

def is_palindrome(num):
    if len(num) <= 1:
        return True
    beg, mid, end = num[0], num[1:len(num)-1], num[-1]
    return (beg == end) and is_palindrome(mid)

def get_square(num):
    if math.sqrt(num) == int(math.sqrt(num)):
        return int(math.sqrt(num))
    return None

def getNums(a, b):
    count = 0
    for i in range(int(a), int(b) + 1):
        if is_palindrome(str(i)) and get_square(i) and is_palindrome(str(get_square(i))):
            count += 1
    return str(count)

test_num = input()
for i in range(test_num):
    a, b = raw_input().strip().split(' ')
    print "Case #" + str(i + 1) + ":", getNums(a, b)
