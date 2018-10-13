# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:17:10 2017

@author: ASUS
"""

FILENAME = 'B-small-attempt1.in'
def helper(r, y, b, now):
    if now == 'R':
        if y > b:
            return 'Y'
        else:
            return 'B'
    elif now == 'Y':
        if r > b:
            return 'R'
        else:
            return 'B'
    else:
        if r > y:
            return 'R'
        else:
            return 'Y'

def stable(n, r, y, b):
    if n > 1 and (r > (y + b) or y > (r + b) or b > (r + y)):
        return 'IMPOSSIBLE'
    current = ''
    if r > y and r > b:
        now = 'R'
        r = r - 1
    elif y > b:
        now = 'Y'
        y = y - 1
    else:
        now = 'B'
        b = b - 1
    current = current + now
    
    for i in range(n-1):
        result = helper(r, y, b, now)
        current = current + result
        if result == 'R':
            r = r - 1
        elif result == 'Y':
            y = y - 1
        else:
            b = b - 1
        now = result
    
    if current[0] == current[-1]:
        current = current[:-2] + current[-1] + current[-2]
    return current
        
    
fr = open(FILENAME, 'r')
fw = open('outputBs.txt', 'w')

t = fr.readline()
t = int(t.strip())

for i in range(t):
    
    case = fr.readline().split()
    
    n = int(case[0])
    r = int(case[1])
#    o = int(case[2])
    y = int(case[3])
#    g = int(case[4])
    b = int(case[5])
#    v = int(case[6])
    
    current = ''
    k = stable(n, r, y, b)
    
    fw.write("Case #{}: {}\n".format(i+1, k))

fr.close()
fw.close()