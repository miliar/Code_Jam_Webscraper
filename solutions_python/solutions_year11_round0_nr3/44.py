import sys

def get_line():
    return sys.stdin.readline().strip()

def read_nums():
    return [int(item) for item in get_line().split(" ")]

def solve( bags ):
    bits = 0
    for num in bags:
        bits ^= num
    if bits != 0:
        return "NO"
    return sum(bags) - min(bags)

(T,) = read_nums()
for test in range(1, T+1):
    (N,) = read_nums()
    bags = read_nums()
    res = solve( bags )
    print "Case #%d: %s" % (test, res)

