#!/usr/bin/env python
import math
import time
begin = time.time()
def getRecycles(d, a, b):
    shift = '%d' % d
    size = len(shift)
    res = [d]
    for n in range(0, size - 1):
        shift = shift[-1] + shift[0:-1]
        if shift[0] != '0':
            recycle = int(shift)
            if recycle >= a and recycle <= b and res.count(recycle) == 0:
                res.append(recycle)
    #res.sort()
    return res

#res = getRecycles(15, 10, 40)
#print res



def isExist(d):
    global recyclelist
    for i in recyclelist:
        if i.count(d) > 0:
            return True
    return False

#a = 1111
#b = 2222

#c = 0
#recyclelist = []

#for d in xrange(a, b + 1):
#    if isExist(d) == False:
#        #c = c + 1
#        r = getRecycles(d, a, b)
#        if len(r) > 1:
#            recyclelist.append(r)
#    
#print 'loop times: %d' % c
#print recyclelist
#
#res = 0
## Cnm = n!/(2!(n-2)!)
#for i in recyclelist:
#    n = len(i)
#    res = res + math.factorial(n) / (2 * math.factorial(n-2)) 
#
#print res
#
#


fh = file('input.txt', 'r')
t = fh.readline()
t = t.replace('\n', '')
print t
t = int(t)

out = file('out.txt', 'w')


for case in range(0, t):
    line = fh.readline()
    line = line.replace('\n', '')
    line = line.split(' ')
    a = int(line[0])
    b = int(line[1])
    
    
    recyclelist = []
    for d in xrange(a, b + 1):
        if isExist(d) == False:
            #c = c + 1
            r = getRecycles(d, a, b)
            if len(r) > 1:
                recyclelist.append(r)

    #print recyclelist

    res = 0
    # Cnm = n!/(2!(n-2)!)
    for i in recyclelist:
        n = len(i)
        res = res + math.factorial(n) / (2 * math.factorial(n-2)) 

    #print res
    
    
    print 'Case #%d: %d' % (case+1, res)
    out.write('Case #%d: %d\n' % (case+1, res))
    

out.close()
fh.close()
end = time.time()
print end - begin
