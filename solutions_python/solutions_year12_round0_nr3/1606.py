import sys

def is_recycled(n, m):
    if n == m:
        return False
    ms = str(m)
    l = len(ms)
    for i in range(l):
        if int(ms[l-(i+1):] + ms[0:l-(i+1)]) == n:
            return True
    return False

def solve(l, casen):
    a, b = map(int, l.split(' '))
    c = 0
    for n in range(a, b+1):
        for m in range(n, b+1):
            c += 1 if is_recycled(n, m) else 0
    print("Case #%d: %d" % (casen, c))

if __name__ == '__main__':
    with open(sys.argv[1], 'rU') as f:
        lines = f.readlines()
        ncases = int(lines[0])
        lines = lines[1:]
        for i in range(ncases):
            solve(lines[i].strip(), i+1)

