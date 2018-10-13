'''
Created on Apr 26, 2013

@author: Sean
'''
from decimal import *
from math import sqrt
from math import floor
getcontext().prec = 50
fin = open('A-small.in', 'r')
finput = fin.readlines()
fin.close()

it = iter(finput)

numbCases = (int)(it.next())

output = ""

for case in xrange(numbCases):
    line = (it.next().rstrip().split())
    r = Decimal(line[0])
    t = Decimal(line[1])
    #res = (-2.0 * r + 1) + sqrt((2.0*r - 1) * (2.0*r - 1) + 8*t)
    #res = res / 4.0
    res = -2 * r + 1
    sqres = 2 * r - 1
    sqres = sqres * (2 * r - 1)
    sqres = sqres + 8*t
    sqres = sqres.sqrt()
    res = res + sqres
    res = res / Decimal(4.0)
    
    ans = float(res)
    
    answer = int(floor(ans))
    
    #answer = int(floor(res))
    
    output += "Case #%d: %d\n" % (case+1, answer)
    
    
fout = open('small.txt', 'w')
fout.write(output)
fout.close
