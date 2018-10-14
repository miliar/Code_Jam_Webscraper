t = int(raw_input())

from itertools import izip

def istidy(num):
    strs = str(num)
    it1 = iter(strs)
    it2 = iter(strs)
    next(it2)
    return all(int(x) <= int(y) for x, y in izip(it1, it2))
   
for t in range(0,t):
    no = int(raw_input())
    while no>=0:
        if(istidy(no)):
            print "Case #%d: %d" % (t + 1, no)
            break
        no = no-1
