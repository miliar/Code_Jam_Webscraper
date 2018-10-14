fl = open('3.log', 'r')
f = open('3.in', 'r')
o = open('3.out', 'w')

L = list()
for line in fl.xreadlines():
    L.append(int(line))
fl.close()

T = int(f.readline().strip())

for t in xrange(T):
    (n, m) = map(int, f.readline().strip().split(' '))
    c = 0
    for x in L:
        if x >= n and x <= m:
            print "--->%d" %x
            c += 1
    
    res = str(c) 
    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)
