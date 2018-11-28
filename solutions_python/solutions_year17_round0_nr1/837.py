def flip(pancake, start, size):
    for j in xrange(start, start + size):
        pancake[j] = 1 - pancake[j]

def countflip(pancake, size):
    pancake = [(1 if p == "+" else 0) for p in pancake]
    N = len(pancake) - size
    flips = 0
    for i in xrange(0, N + 1):
        if pancake[i] == 0:
            flip(pancake, i, size)
            flips += 1
    if all(p for p in pancake[N:]):
        return str(flips)
    return "IMPOSSIBLE"

for t in xrange(input()):
    pancake, size = raw_input().split()
    print "Case #%d: %s" % (t + 1, countflip(pancake, int(size)))
