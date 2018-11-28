#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

input = 'B-large.in'
output = 'B-large.out'
f = file(input)
g = file(output,'w')

##

f = file(input)
g = file(output,'w')

n_cases = int(f.readline().strip())

for k in range(n_cases):
       
    line = f.readline().strip()
    
    num = [int(x) for x in list(str(line))]
    print num
    
    numlist = sorted([ x for x in num if x != 0 ])
        
    # compare 2 digit
    l = len(num)
    max = sorted(num, reverse=True)
    if num == max:
        num.append(0)
        c = numlist[0]
        num.remove(c)
        num = [c]+sorted(num) # answer
        answer = num
    else:
        for i in range(l-1,0,-1):
            left = num[i-1]
            right = num[i]
            if left == 0 and not right == 0:
                a = num[i:l]
                b = [x for x in a if x > 0]
                c = min(b)
                num[i-1] = c
                a.append(0)
                a.remove(c)
                a.sort()
                num = num[0:i] + a # answer
                answer = num
                break
            if right > left:
                a = num[i:l]
                b = [x for x in a if x > left]
                c = min(b)
                num[i-1] = c
                a.append(left)
                a.remove(c)
                a.sort()
                num = num[0:i] + a # answer
                answer = num
                break
    
    answer = "".join([str(x) for x in answer])

    result = "Case #%d: %s\n" % (k+1, answer)
    print result,
    g.write(result)

f.close()
g.close()

