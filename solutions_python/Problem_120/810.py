import sys,os
f = open(sys.argv[1],"r")
num_pro = int(f.readline())
n = 1
for line in f:
    if len(line) < 2:
        break
    tmp = line.split()
    r = int(tmp[0])
    t = int(tmp[1])
    s = 2*r + 1
    cnt = 0
    while s <= t:
        cnt += 1
        r += 2
        s += 2*r + 1
    print "Case #" + str(n) + ": " + str(cnt)
    n += 1
    
