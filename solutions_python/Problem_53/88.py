import sys
import fileinput

i=0
for line in fileinput.input():
    if i>0:
        n,k = line.split(' ')
        n = int(n)
        k = int(k)
        a = 2 ** n
        k = k % a
        if k==a-1:
            print 'Case #%d: ON' % i
        else:
            print 'Case #%d: OFF' % i
    i+=1



