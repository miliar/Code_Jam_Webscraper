import sys

LIM = 10**7

fairandsquare = []

def ispal(i):
    s = str(i)
    return s == s[::-1]

c = 0
for i in xrange(1,LIM+1):
    if ispal(i) and ispal(i*i):
        fairandsquare.append(i*i)

for i in xrange(1, 1+int(sys.stdin.readline())):
    l = sys.stdin.readline().replace("\n", "").split(" ")
    A, B = map(int, l)
    c = 0

    for num in fairandsquare:
        if num > B:
            break
        if num >= A:
            c += 1
    print "Case #%d: %d" % (i, c)
