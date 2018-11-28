import sys

f = open(sys.argv[1], "r")
loop = int(f.readline().rstrip('\n'))

for i in range(loop):
    n = 0
    s = 0
    d = f.readline().rstrip('\n').split(' ')
    max = int(d[0])+1
    for j in range(0,max):
        x = int(d[1][j])
        if x > 0 and s < j:
                n += j-s
                s += j-s
        s += x
    print "Case #%d: %d" % (i+1, n)


f.close()

