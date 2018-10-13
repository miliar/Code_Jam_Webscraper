# CodeJam 2013 By Chonnakan Rittinon

import math

def is_palindome(s):
    if len(s) == 1:
        return True
    head = 0
    tail = len(s)-1
    while tail>head:
        if s[head] != s[tail]:
            return False
        head = head + 1
        tail = tail - 1
    return True

n = int(raw_input())
for i in range(0,n):
    s = raw_input()
    a = int(s.split(' ')[0])
    b = int(s.split(' ')[1])
    
    j = int(math.ceil(math.sqrt(a)))
    count = 0
    while j*j<=b:
        if is_palindome(str(j*j)):
            if is_palindome(str(j)):
                count = count + 1
        j = j + 1
    print ('Case #%s: %s')%(i+1,count)



