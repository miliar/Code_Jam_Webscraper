import os
import math

inHandle = open('input.txt','r')
outHandle = open('output.txt','w')

nCases = int(inHandle.readline().replace('\n',''))

for case in range(nCases):
    (r,t) = tuple([int(x) for x in inHandle.readline().split(' ')])
    a = 2
    b = (2*r - 1)
    c = 0 - t

    ans = int(max((0 - b + math.sqrt(b**2 - 4 * a * c)) / (2 * a), (0 - b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)))

    if(t < 2 * ans * ans + 2 * r * ans - ans):
        ans = ans - 1
        
    outHandle.write('Case #' + str(case+1) + ': ' + str(ans) + '\n')

inHandle.close()
outHandle.close()
