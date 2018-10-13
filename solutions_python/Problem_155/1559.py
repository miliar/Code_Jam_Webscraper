import sys

sys.stdin.readline()
for t, s in enumerate(sys.stdin, 1):
    up = 0
    invite = 0
    for i, c in enumerate(s.split()[1]):
        x = int(c)
        if up >= i:
            up += x
        else:
            invite += i - up
            up = i + x
    print "Case #{}: {}".format(t, invite)
