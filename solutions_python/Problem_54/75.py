from fractions import gcd

def GCD(l):
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return gcd(l[0], l[1])
    else:
        return GCD([gcd(l[0], l[1])] + l[2:])

data = []
for line in open('data.txt', 'r'):
    l = line.split('\n')[0].split(' ')
    data.append([long(n) for n in l[1:]])
data = data[1:]

for n in xrange(len(data)):
    l = data[n]
    l.sort()
    d = []
    for i in xrange(len(l)-1):
        d.append(l[i+1] - l[i])

    T = GCD(d);
    if T == 1 or l[0] % T == 0:
        y = 0
    else:
        y = T - l[0] % T
    print "Case #%d: %d" % (n+1, y)