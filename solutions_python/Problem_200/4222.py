#!usr/bin/python

import re

def is_sorted(a):

    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

n = int(raw_input())

for line in range(n):
    N = int(raw_input())
    result = 0

    #for num in range(N, 0, -1):
    num = N
    while num != 0:
        #print num
        if re.match("^[1]{2,}[0]+$", str(num), re.MULTILINE):
            #print str(num), "=+"
            _num = str(num * 10)
            num = int(_num[1:])
            #print str(num), "+"
            #continue

        if is_sorted([int(i) for i in str(num)]):
            result = num
            break
        num -= 1
    print "Case #" + str(line + 1) + ": " + str(result)
