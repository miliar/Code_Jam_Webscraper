f = open('input.txt')
o = open('output.txt','w+')
t = int(f.readline())
for i in range(t):
    l = f.readline()
    tot = 0
    inv = 0
    sm = int(l.split()[0])
    s = l.split()[1]
    for x in range(sm + 1):
        ns = int(s[x])
        if ns != 0:
            if x > tot:
                dif = x - tot
                inv += dif
                tot += dif
            tot += ns
    o.write('Case #%d: %d \n' % ((i+1), inv))
f.close()
o.close()