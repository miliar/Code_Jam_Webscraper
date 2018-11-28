# -*- coding: utf-8 -*-
#!/usr/bin/python 

import math

def isPal(x):
    xarr = []
    while x>0:
        xarr.append(int( x % 10))
        x = math.floor(x / 10)
    
    #print 'x ve xarr', x,xarr
    #print range(int(len(xarr) / 2)+1) 
    
    pal = [ xarr[i] == xarr[len(xarr) - i - 1] for i in range(int(len(xarr) / 2)+1)]
    
    return all(pal)
    

inp = open("C-small-attempt0.in", "r")
out = open("output", "w")

testCases = int( inp.readline())

for i in range(testCases):

    count = 0
    lower, upper = [int(x) for x in inp.readline().split()]
    #print lower, upper
    #print range(int(math.ceil(math.sqrt(lower))), int(math.floor(math.sqrt(upper))) + 1)
    for j in range(int(math.ceil(math.sqrt(lower))), int(math.floor(math.sqrt(upper))) + 1):
        if isPal(j) and isPal(j ** 2):
            count += 1
            
    out.write("Case #{}: {}\n".format(i + 1,count))        
    print count