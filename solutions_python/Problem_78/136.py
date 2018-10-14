'''
Created on May 20, 2011

@author: herman
'''
from string import split

infile = open("large_input.txt","r")
outfile = open("large_output.txt","w")

trials = int(infile.readline())

def factors(x,lst):
    if x == 1:
        return lst
    else:
        for y in xrange(2,x+1):
            if x % y == 0:
                lst.append(y)
                return factors(x/y,lst)

for i in xrange(trials):
    nums = [int(x) for x in split(infile.readline())]
    N = nums[0]
    Pd = nums[1]
    Pg = nums[2]
    flst = factors(100,[1])
    if Pd == 0:
        prod = 1
    else:
        for m in factors(Pd,[1]):
            if flst.count(m) > 0:
                flst.remove(m)
            prod = 1
        for j in flst:
            prod = prod*j
    if (prod <= N):
        result = "Possible\n"
    else:
        result = "Broken\n"
    if (Pg == 100 or Pg == 0):
        if Pd != Pg:
            result = "Broken\n"
    s = "Case #%d: " % (i+1)
    s = s + result
    outfile.write(s)
    print s
    
infile.close()
outfile.close()
