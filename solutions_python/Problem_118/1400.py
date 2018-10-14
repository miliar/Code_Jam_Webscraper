#!/usr/bin/python

lst = []
sz = 100

def isPal(item):
    for i in range(len(item)/2):
        if item[i] != item[len(item)-i-1]:
            return False
    return True

def expandFast(item):
    if len(item) > sz/2:
        return
        
    lst.append(item)
    expandFast('1'+item+'1')    
    expandFast(item+item)

def expand(item):
    if len(item) > 7:
        return

    lst.append(item)
    for i in range(1,10):
        expand(str(i)+item+str(i))
        
    if item[0] != '0':
        expand(item+item)

for i in range(10):
    expand(str(i))

expandFast('0')
expandFast('1')


pals = [pow(int(x),2) for x in lst if isPal(str(pow(int(x),2)))]
pals = list(set([x for x in pals if x > 0]))
pals.sort()


fp = open('p3.in')
cases = int(fp.readline())
cc = 1

while cases > 0:
    n, m = [int(x) for x in fp.readline()[0:-1].split(' ')]
    
    print "Case #%d: %d" % (cc, len([x for x in pals if x >= n and x <= m]))
        
    cc = cc + 1
    cases = cases - 1

