__author__ = 'sware'

import sys

handle = file(sys.argv[1])
handleout = file(sys.argv[2], 'w')

def digitize(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n /= 10
    return digits

for k in xrange(int(handle.readline())):
    N = int(handle.readline())
    digs = digitize(N)
    while True:
        found = True
        n = 0
        for i in reversed(xrange(len(digs)-1)):
            if digs[i] < digs[i+1]:
                found = False
                for j in xrange(i+1):
                    digs[j] = 9
                digs[i+1] -= 1
                break
            n += digs[i+1]
            n *= 10
        n += digs[0]
        if found:
            break
    handleout.write('Case #{}: {}\n'.format(k+1, n))