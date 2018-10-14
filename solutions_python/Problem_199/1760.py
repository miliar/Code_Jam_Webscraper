import sys

data = sys.stdin.readlines()
t = int(data[0])
for i in range(t):
    print "Case #%d:" % (i+1),

    d = data[i+1].split()

    st = d[0]
    p = []
    for c in st:
        if c == '+':
            p.append(True)
        elif c == '-':
            p.append(False)

    s  = int(d[1])

    ret = 0

    for j in range(len(p) - s + 1):
        if not p[j]:
            for k in range(s):
                p[j+k] = not p[j+k]
            ret += 1

    if False in p:
        print "IMPOSSIBLE"
    else:
        print "%d" % ret
        
