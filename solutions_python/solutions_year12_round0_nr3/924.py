import sys

def isrecycle(xi, yi):
    x = str(xi)
    y = str(yi)
    if len(x) != len(y): return False
    for diff in range(1, len(x)):
        if x == y[diff:] + y[:diff]: return True
    return False

def solve(A, B):
    ans = 0
    for i in range(A, B+1):
        for j in range(i+1, B+1):
            if isrecycle(i, j): ans = ans + 1
    return ans

f = sys.stdin
T = int(f.readline().strip())
lines = f.readlines()

assert isrecycle(12345, 51234)
assert isrecycle(12345, 45123)
assert isrecycle(12345, 34512)
assert isrecycle(12345, 23451)
assert not isrecycle(12345, 25134)

for i, line in enumerate(lines):
    A, B = [int(x) for x in line.strip().split()]
    print "Case #%d: %d" % (i + 1, solve(A, B))
