#!/usr/bin/env python

for t in xrange(1, input()+1):
    fckingval = list(str(int(raw_input(), 10)))

    for idx in xrange(len(fckingval)-2, -1, -1):
        a, b = int(fckingval[idx]), int(fckingval[idx+1])
        if a > b:

            fckingval[idx] = str(a-1)
            for j in xrange(idx+1, len(fckingval)):
                if fckingval[j] == '9': break
                else: fckingval[j] = '9'

    while fckingval[0] == '0': fckingval.pop(0)
    res = ''.join(fckingval)

    print 'Case #{}: {}'.format(t, res)
