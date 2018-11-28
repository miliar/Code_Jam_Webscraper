'''
Created on Apr 12, 2013

@author: uglytroll
'''
import math


def possible_count(start, end):
    result = 0
    ss = math.sqrt(start)
    if ss % 1 == 0:
        start_sqrt = int(ss)
    else:
        start_sqrt = int(math.ceil(ss))
    es = math.sqrt(end)
    if es % 1 == 0:
        end_sqrt = int(es)
    else:
        end_sqrt = int(math.ceil(es) - 1)
#     print 'start : %d, end : %d' % (start_sqrt, end_sqrt)
    for num in xrange(start_sqrt, end_sqrt + 1):
        if num in possible:
            result += 1
#             print 'possbile : %d' % num 
            continue
        if num in not_possible:
            continue
        if is_palindrome(num) and is_palindrome(num * num):
            result += 1
#             print 'possbile : %d' % num 
            possible.add(num)
        else:
            not_possible.add(num)
    return result


def is_palindrome(num):
    a = str(num)
    b = a[::-1]
    return a == b

f = open('/home/uglytroll/codejam/2013/qual/3.in', 'r')
o = open('/home/uglytroll/codejam/2013/qual/3.out', 'w')

T = int(f.readline().strip())
possible = set([])
not_possible = set([])

for t in xrange(T):
    start, end = map(int, f.readline().strip().split(' '))
    result = possible_count(start, end)
    s = "Case #%d: %s\n" % (t+1, result)
#     print s
    o.write(s)
    