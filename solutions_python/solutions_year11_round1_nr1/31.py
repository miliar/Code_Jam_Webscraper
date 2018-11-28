import sys

def get_line():
    return sys.stdin.readline().strip()

def read_nums():
    return [int(item) for item in get_line().split(" ")]

def solve(N, Pd, Pg):
    if Pg == 100 and Pd != 100:
        return False
    if Pg == 0 and Pd > 0:
        return False
    d = 1
    while Pd % 2 == 0 and d < 4:
        Pd /= 2
        d*= 2
    while Pd % 5 == 0 and d < 100:
        Pd /= 5
        d*= 5
    return N >= (100 / d)

(T,) = read_nums()
for test in range(1, T+1):
    (N, Pd, Pg) = read_nums();
    if solve(N, Pd, Pg):
        print "Case #%d: Possible" % (test,)
    else:
        print "Case #%d: Broken" % (test,)

