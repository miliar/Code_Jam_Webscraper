
from math import *
s = '''29
15
9
2
3
11
27
5
26
6
14
13
17
19
10
7
21
29
16
22
8
28
23
30
18
24
20
12
25
4'''

import tools

import decimal
def distance(p1, p2):
    return sqrt((p1[1] - p2[1])**2 + (p1[0] - p2[0])**2)

def point_in_circle(point, radius):
#    print point
    return distance(point, [0, 0]) <= radius


s = s.split("\n")
index = 0
context = decimal.Context(prec=600, rounding=decimal.ROUND_HALF_DOWN)

for case in range(int(s[0])):
    index += 1    
    n = int(s[index])

    f = decimal.Decimal('5')
    f = f.sqrt(context)
    f = f + decimal.Decimal('3')
    g = f

    for i in range(n-1):
        f = f * g
        
    out = str(f.normalize(context))
    out = '000'+out
    
    digits = out[out.find('.')-3:out.find('.')]
    
    
#    print f*100
    
    print 'Case #%i: %s'%((case+1),(digits))
    
        
    
    


