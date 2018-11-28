import sys
f = open(sys.argv[1])
num_cases = int(f.next())
on_or_off = {True : 'ON', False : 'OFF'}
for i in xrange(1, num_cases + 1):
    n, k = f.next().split(' ', 2)
    n = long(n)
    k = long(k)
    on_off = on_or_off[(2 ** n - 1) == k % (2 ** n)]
    print 'Case #%i: %s'%(i, on_off)
    

