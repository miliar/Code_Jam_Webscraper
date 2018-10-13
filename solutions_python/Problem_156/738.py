import math
import sys


#fin = sys.arg[1]
fin = "./B-small-attempt2.in"
#fin = "./b.in"

with open(fin) as f:
    lines = f.readlines()

def divisions(m):
    for i in range(1,m/2+1):
        yield i, m-i

def divide(m):
    if m % 2 == 1:
        return m/2+1, m/2
    return m/2, m/2

def shouldDoDivision(v):
    pos = -1
    m = v[pos]
    a, b = divide(m)
    ops = 1
    #print "initial m = ", m, "a", a, "ops", ops

    while a + ops < m:
        pos -= 1
        if not (abs(pos) <= len(v)):
            return True
        nm = v[pos]
        #print "nm", nm, "ops", ops, "a", a
        if (nm + ops) < a:
            return True
        if (nm + ops) < m:
            return True

        a, b = divide(nm)
        ops += 1
    return False


from collections import deque
for case, ln in enumerate(range(1, len(lines), 2)):

    d = lines[ln]
    pancakes = map(int, lines[ln+1].split())
    pancakes = sorted(pancakes)

    f = (pancakes,0)
    queue = deque([f])
    while True:
        n = queue.popleft()
        pan, i = n
        npan = []
        for p in pan:
            p -= 1
            if p > 0:
                npan.append(p)

        if len(npan) == 0:
            ans = i
            break

        s1 = (npan[:],i+1)
        queue.append(s1)

        npan = sorted(pan)
        gen = divisions(npan[-1])

        del npan[-1]
        for a,b in gen:
            s2 = (npan + [a,b], i+1)
            queue.append(s2)


    print "Case #%d: %d" % (case + 1, ans + 1)

