import sys

input = open(sys.argv[1])
num = int(input.next())

for i in range(num):
    n, k = [int(a) for a in input.next().split()]
    
    r = 2 ** n
    
    q = k % r
    
    if q == r - 1:
        result = 'ON'
    else:
        result = 'OFF'
    
    print 'Case #%d: %s' % (i+1, result)
    
    