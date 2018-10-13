import sys 
from math import floor, ceil

lines = sys.stdin.readlines()
for i in range((int(lines[0]))):
    m = [int(x) for x in lines[2*(i+1)].split()]
    a1 = 0
    a2 = 0
    diff = []
    for j in range(len(m)-1):
        if m[j] > m[j+1]: 
            a1 += m[j] - m[j+1]
            diff.append(m[j] - m[j+1])
    if len(diff):
        mm = max(diff)
        for j in range(len(m)-1):
            a2 += min(m[j],mm)
    print 'Case #' + str(i+1) + ': ' + str(a1) + ' ' + str(a2)
