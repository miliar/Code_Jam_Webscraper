import sys
import bisect
import math



def isp(n):
    s = str(n)
    return s == s[::-1]



fs = [1, 4, 9, 121, 484]

# No idea why this works mathematically, but it follows a pattern

prev = ['1', '2']
for d in range(1,30):
    next = []
    for p in prev:
        for c in '012':
            n1 = int(p + c + p[::-1])**2
            n2 = int(p + c + c + p[::-1])**2
            w = False
            if isp(n1):
                fs.append(n1)
                w = True
            if isp(n2):
                fs.append(n2)
                w = True
            if w:
                next.append(p + c)
    prev = next


fs.sort()

print(fs[:10], file=sys.stderr)
print(len(str(fs[-1])), file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1,T+1):
    board = []
    A, B = map(int, fin.readline().split())

    i = bisect.bisect_left(fs, A)
    j = bisect.bisect_right(fs, B)

    print("Case #%d: %s" % (case, j-i))


