#f = open("/home/roy/in.txt")
f = open("/home/roy/Downloads/B-large.in")

lines = f.readlines()
count = int(lines[0])

#print "There are %s cases" % count

import math

idx = 1
for i in range(0, count):
    line1 = lines[idx]
    idx = idx + 1

    [L, P, C] = [int(a) for a in line1.rstrip().split(" ")]
    t = math.log(P/float(L), C)
    t = math.log(t, 2)    
    ans = int(math.ceil(t))
    if ans < 0:
        ans = 0
    
    print "Case #%d: %s" % (i+1, str(ans))
