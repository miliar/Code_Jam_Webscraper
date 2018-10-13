from math import *

def gcd(a, b):
    if (a<b): a,b=b,a
    while (b>0):
        c=a%b
        a=b
        b=c
    return a

fin = open('B-large.in','r')
fout = open('B-large.out','w')
#fin = open('warning.in','r')
#fout = open('warning.out','w')
n = int(fin.readline())
for t in xrange(1,n+1):
    print "%d/%d"%(t,n)
    line = list(set(map(int, fin.readline().strip().split(' '))[1:]))
    line.sort()
    D = line[1]-line[0]
    g = D
    for i in xrange(2,len(line)):
        d=line[i]-line[i-1]
        g=gcd(g,d)
    k=(line[0]-1)/g+1
    fout.write('Case #%d: %d\n'%(t, k*g-line[0]))
fin.close()
fout.close()    
