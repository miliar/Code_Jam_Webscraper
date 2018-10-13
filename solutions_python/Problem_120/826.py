from math import sqrt, floor

f = open('1.ex', 'r')
fo = open('1.out' ,'w')

cases = int(f.readline())

for case in xrange(cases):
    
    r, t = [int(x) for x in f.readline().split()]
    
    t_1 = (2*r + 1)
    v = 4
    
    a = v/2
    b = t_1 - v/2
    c = -t
    
    D = b**2 - 4*a*c
    n = (-b + sqrt(D))/(2*a)
    
    output = int(floor(n))
    
    fo.write('Case #' + str(case+1) + ': ' + str(output) + '\n')