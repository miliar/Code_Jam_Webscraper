import math, collections
f = open('input.in','r')
g = open('output.txt','w')
"""
consider the binary expansion of k: first people split the row into 2 parts, the first 3 people split it into 4, ..., 
the first 2^n-1 people split it into 2^n parts
"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    n, k = [int(x) for x in f.readline()[:-1].split(' ')]
    p = len(bin(k)) - 2
    divisor = 2**(p-1)
    k_left = k - divisor + 1
    q, m_large = divmod(n - divisor + 1, divisor)
    m_small = q - m_large
    if k_left <= m_large:
        result = ' '.join( [ str((q+1)/2), str(q/2) ] )
    else:
        result = ' '.join( [ str(q/2), str((q-1)/2) ] )
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()