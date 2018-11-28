import math
#f = open('test')
f = open('B-large.in')
for x in range(int(f.readline())):
    l = f.readline().split()
    C, F, X = float(l[0]), float(l[1]), float(l[2])
    threshhold = (X - C) * F / C
    NUM = max(0, int(math.ceil((threshhold - 2) / F)))
    res = 0
    for i in range(NUM):
        res += C / (2 + i * F)
    res += X / (2 + F * NUM)
    #print threshhold, NUM, res
    print 'Case #%d: %.7f' % (x + 1, res)
f.close()


