from sys import stdin

for case in range(1, int(stdin.readline()) + 1):
    n = int(stdin.readline())
    c = [int(x) for x in stdin.readline().split()]
    bits = [0] * 20
    minc = 1000000

    for x in c:
        i = 0
        while x > 0:
            bits[i] ^= (x & 1)
            x >>= 1
            i+=1

    if 1 in bits:
        print "Case #%d: NO" % case
    else:
        print "Case #%d: %d" % (case, sum(c) - min(c))
