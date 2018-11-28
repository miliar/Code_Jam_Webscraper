#!/usr/bin/python

input_file = 'B-large.in'
lines = []
with open(input_file,'r') as f:
    lines = [int(i.strip()) for i in f.readlines()]

def is_tidy(a):
    str_a = str(a)
    for i in xrange(len(str_a)-1):
        x = int(str_a[i])
        y = int(str_a[i+1])
        if x > y:
            return False, i
    return True, None

def solve(n):
    ok, pos = is_tidy(n)
    if ok:
        return n
    
    i = pos
    m = str(n)
    x = m[i]
    y = m[i+1]
    l = list(m)
    l[i] = str(int(l[i])-1)
    for j in xrange(i+1, len(m)):
        l[j] = '9'
    o = int(''.join(l))
    
    return solve(o)

for i in xrange(lines[0]):
    print "Case #{}: {}".format(i+1, solve(lines[i+1]))
