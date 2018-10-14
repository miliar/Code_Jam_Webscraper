import itertools, math
f = open('i2.txt', 'r')
g = open('o2.txt', 'w')
lines = f.readlines()
c = 1
for t in xrange(int(lines[0].strip())):
    n, k = map(int, lines[c].split())
    s = float(lines[c+1])
    a = map(float, lines[c+2].split())
    c += 3
    res = 1
    while (True):
        x = sum(a) + s
        curr = (x/n)
        b = a[:]
        for e in b:
            if (e >= curr):
                a.remove(e)
                n -= 1
                res *= e
        if (len(a) == 0 or len(a) == len(b)):
            break
    ans = curr**n * res
    print ans
    g.write("Case #"+str(t+1)+": "+str(ans)+'\n')
        
f.close()
g.close()
