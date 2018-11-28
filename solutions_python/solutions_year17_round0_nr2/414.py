T = int(raw_input())

def Tidy(a):
    pos = 0
    while pos < len(a) - 1 and a[pos] <= a[pos + 1]:
        pos += 1
    if pos == len(a) - 1:
        return 0
    return pos + 1

def Adjust(a, pos):
    l = len(a)
    for i in range(pos, l):
        a[i] = 9
    a[pos - 1] -= 1
    if a[0] == 0:
        a = a[1:]
    return a

for t in xrange(1, T + 1):
    a = [ord(x) - ord('0') for x in raw_input()]
    pos = Tidy(a)
    while pos != 0:
        a = Adjust(a, pos)
        pos = Tidy(a)
    print "Case #%d: %s" % (t, ''.join([str(x) for x in a]))
