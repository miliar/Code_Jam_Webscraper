from sys import stdin

def riadok():
    return map(int, stdin.readline().split())

for cas in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = riadok()
    b = reduce(lambda x, y: x ^ y, a)
    print "Case #%d: " % (cas + 1),
    if b != 0:
        print "NO"
    else:
        print sum(a) - min(a)
