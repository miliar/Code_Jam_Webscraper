'''
Created on Oct 15, 2012

@author: mengda
'''

def process(X, Y):
    rlt = ''
    m = 1
    flag = 1
    x = y = 0
    while not x == X:
        x += m * flag
        if flag == 1:
            rlt += 'E'
        else:
            rlt += 'W'
        flag *= -1
        m += 1
    if Y > 0:
        flag = -1
    else:
        flag = 1
    while not y == Y:
        y += m * flag
        if flag == 1:
            rlt += 'N'
        else:
            rlt += 'S'
        flag *= -1
        m += 1
    return rlt

f = open('B-small-attempt0.in', 'r')
# f = open('1B_B_t.in', 'r')
T = int(f.readline())
outLine = []

for i in range(1, T + 1):
    (X, Y) = map(int, f.readline().split())
    outLine.append('Case #%d: %s\n' % (i, process(X, Y)))
    print outLine[-1],

f.close()
outFile = open('B.out', 'w')
outFile.writelines(outLine)
outFile.close()
