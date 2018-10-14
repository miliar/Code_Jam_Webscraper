#!/usr/bin/env python

def compute(a):
    res = ""
    if len(a) == 1:
        return a
    for i in xrange(len(a)-1):
        if int(a[i+1]) >= int(a[i]):
            res = res+a[i]
            if (i+1) == (len(a)-1):
                res=res+a[i+1]
        else:
            res = compute(res+str(int(a[i])-1)+'9')+'9'*(len(a)-i-2)
            break
    return res.lstrip("0")

o = open('output', 'w')
f = open('input', 'r')
n = int(f.readline().strip())

for i in xrange(n):
    o.write("Case #{}: {}\n".format(i+1, compute(f.readline().strip())))

o.close()
f.close()
