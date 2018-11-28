import math

nt = int(input())
for it in xrange(nt):
    ds = raw_input()
    ds = map(lambda d: int(d), ds)
    n = len(ds)
    sw = False
    for i in xrange(n):
        if sw:
            ds[i] = 9
        elif i+1 < n and ds[i+1] < ds[i]:
            sw = True
            ds[i] -= 1
    for i in xrange(n-1,0,-1):
        if ds[i-1] > ds[i]:
            ds[i] = 9
            ds[i-1] -= 1
    i = 0
    while i < n and ds[i] == 0: i+= 1    
    if ds[0] == 0: ds = ds[i:]
    
    resp = "".join(map(lambda d: str(d) ,ds))
    print "Case #{}: {}".format(it+1, resp)