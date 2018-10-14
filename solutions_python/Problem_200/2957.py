import sys

def check_right(n):
    pos = 0
    last = 0
    while pos < len(n):
        if n[pos] < last:
            return pos
        last = n[pos]
        pos += 1
    return pos

def fix_left(n, pos):
    old_pos = pos
    pos -= 1
    while pos > -1:
        if pos == 0:
            n[pos] -= 1
            return fix_after(n, pos)
        elif n[pos]-1 >= n[pos-1]:
            n[pos] -= 1
            return fix_after(n, pos)
        pos -= 1

def fix_after(n, pos):
    pos += 1
    for i in range(pos, len(n)):
        n[i] = 9
    return n

def prep(n):
    return str(int("".join([str(x) for x in n])))

def sol(n):
    n = str(int(n))
    n = [int(x) for x in list(n)]
    pos = check_right(n)
    if pos == len(n):
        return prep(n)
    return prep(fix_left(n, pos))

def reader(filename):
    ret = []
    with open(filename) as f:
        t = int(f.readline())
        for _ in range(t):
            ret.append(f.readline())

    return ret

data = reader(sys.argv[1])
for i in range(len(data)):
    out = sol(data[i])
    print "Case #%d: %s" % (i+1, out)
