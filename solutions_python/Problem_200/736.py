#!/usr/bin/python
import sys, math        

T = int(sys.stdin.readline())
for t in range(T):
    s = sys.stdin.readline().strip()
    ls = list(s)
    result = ''
    mi = 0
    m = ls[0]
    #find last entry that is bigger than its predecessor
    for i in range(len(s)):
        if ls[i] == m:
            continue
        elif ls[i] < m:
            # need to reduce result
            if mi == 0 and ls[mi] == '1':
                result = '9' * (len(s) - 1)
            else:
                ls[mi] = str(int(ls[mi]) - 1)
                result = s[:mi] + ls[mi] + '9' * (len(s) - mi - 1)
            break
        m = ls[i]
        mi = i
    
    if len(result) == 0:
        result = s
    #print(s, result, mi, i)

    print "Case #%d: %s" % ((t + 1), result)
