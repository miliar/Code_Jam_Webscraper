




fd = open("input")
d = fd.read().split("\n")


#First Line
D = int(d[0])


def match(a,b):
    if len(b) == 1:
        return a.count(b)

    c = 0
    for i in xrange(len(a)):
        if a[i] == b[0]:
            c += match(a[i+1:],b[1:])

    return c

Pos =()
for i in xrange(1,D+1):
    print "Case #%d: %04d"%(i,match(d[i], "welcome to code jam"))
