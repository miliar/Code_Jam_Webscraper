import sys

def is_tidy(x):
    return sorted(str(x)) == list(str(x))

def solve(x):
    if is_tidy(x):
        return x
    p = 10
    while True:
        if is_tidy((x/p) * p - 1):
            return (x/p) * p - 1
        p *= 10


lines = sys.stdin.readlines()
for i, l in enumerate(lines[1:]):
    x = int(l.strip())
    print "Case #%d: %d" % ((i+1), solve(x))
