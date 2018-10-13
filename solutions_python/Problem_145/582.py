#!/usr/bin/env python

import sys
import re
from math import log, ceil

from gmpy import mpq

def getl():
    return sys.stdin.readline().strip()

T = int(getl())

rex = re.compile(r'^(\d+)/(\d+)$')

for i in range(T):
    x = i + 1

    data = rex.match(getl().strip()).groups()

    a_ = int(data[0])
    b_ = int(data[1])

    z = mpq(a_) / mpq(b_)

    a = int(z.numer())
    b = int(z.denom())

    n_ = log(b) / log(2)
    ni_ = int(n_)

    n = int(ceil(-1 * log(z) / log(2)))

    if z == 0         or \
       z > 1          or \
       n_ - ni_ != 0  or \
       n > 40         or \
       False :

        print('Case #%i: %s' % (x, 'impossible'))

    else:

        print('Case #%i: %s' % (x, n))


