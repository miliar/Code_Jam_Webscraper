from sys import stdin

def riadok():
    return map(int, stdin.readline().split())

for cas in range(int(stdin.readline())):
    (n, k) = riadok()
    q = (1 << n) - 1
    if (q & k) == q:
        s = "ON"
    else:
        s = "OFF"
    print "Case #%d: %s" % (cas + 1, s)
