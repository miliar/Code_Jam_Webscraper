import os
from functools import reduce

inHandle = open('input.txt','r')
outHandle = open('output.txt','w')

nCases = int(inHandle.readline().replace('\n',''))

for case in range(nCases):
    a = inHandle.readline().split('\n')[0]
    b = inHandle.readline().split('\n')[0]
    c = inHandle.readline().split('\n')[0]
    d = inHandle.readline().split('\n')[0]

    e = a[0] + b[1] + c[2] + d[3]
    f = a[3] + b[2] + c[1] + d[0]

    g = reduce(lambda x,y: x+y, map(lambda x : x[0], [a,b,c,d]))
    h = reduce(lambda x,y: x+y, map(lambda x : x[1], [a,b,c,d]))
    i = reduce(lambda x,y: x+y, map(lambda x : x[2], [a,b,c,d]))
    j = reduce(lambda x,y: x+y, map(lambda x : x[3], [a,b,c,d]))
            
    points = {'X':1, 'O':-1, 'T':0, '.':100}

    cases = [a, b, c, d, e, f, g, h, i, j]

    answer = ''
    for i in cases:
        ans = reduce(lambda x,y: x+y, map(lambda x : points[x], i))
        if(ans == 3 or ans == 4):
            answer = 'X won'
            break
        elif(ans == -3 or ans == -4):
            answer = 'O won'
            break
        elif(ans < -4 or ans > 4):
            answer = 'Game has not completed'
        elif(answer != 'Game has not completed'):
            answer = 'Draw'
            
    inHandle.readline()   
    outHandle.write('Case #' + str(case+1) + ': ' + str(answer) + '\n')

inHandle.close()
outHandle.close()
