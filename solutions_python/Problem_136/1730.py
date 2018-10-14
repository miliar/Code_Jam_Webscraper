__author__ = 'ligenjian'
import math

inputfile = open('data/B.txt')
outputfile = open('output/B.txt','w')

t = int(inputfile.readline())

def score(c,f,x,n):
    sum = 0
    for i in range(n):
        sum += c / (2.0 + i * f)
    return sum + x / (2.0 + n * f)


for i in range(t):
    c,f,x = map(float, inputfile.readline().split(' '))
    mintime = 100000
    for n in range(int(x / c) + 1):
        time = score(c,f,x,n)
        if time < mintime:
            mintime = time
            minn = n
    print>>outputfile, 'Case #%d: %.7f' % (i + 1, mintime)
    print 'iter ',i,' finished'
