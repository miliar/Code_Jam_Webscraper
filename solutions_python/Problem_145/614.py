import os
f_inp = 'inp_1.txt'
f_out = 'out_1.txt'
f=open(f_inp)
f_o = open(f_out, 'w')
from math import log, floor
from fractions import gcd

def next_line(f):
    line = f.readline()
    if line:
        line = line.strip()
    return line

def get_pow_2(n):
    res = 0
    while n%2 == 0:
        res += 1
        n/=2
    return res

def get_closest_pow_2(n):
    res = 0
    while n >= 2.0:
        res += 1
        n/=2
    return res

def get_num(p, q):
    num = None
    x = gcd(p,q)
    p/=x
    q/=x
    print x, p, q
    pow_2 = log(q,2)
    print pow_2
    if int(pow_2) != pow_2:
        return None
    x1 = get_closest_pow_2(p)
    print x1
    num = pow_2 - x1
    return int(num)

num_tc = int(next_line(f))
np = 'impossible'
resp = 'Case #%s: %s'
for i in xrange(1,num_tc+1):
    p,q = [int(_) for _ in next_line(f).split('/')]
    res = get_num(p, q)
    if res is None:
        res = np
    out = resp % (i, res)
    f_o.write('%s\n' % out)
    print out
f.close()
f_o.close()
