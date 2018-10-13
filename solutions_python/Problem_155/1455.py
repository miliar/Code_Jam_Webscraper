import sys

def calc(arr):
    add = 0
    s = 0
    for i, v in enumerate(arr):
        if s< i:
            add += i-s
            s += i-s + v
        else:
            s += v
    return add

f = open(sys.argv[1])
cases = int(f.readline().strip())
for i in xrange(1, cases + 1):
    case = f.readline().strip().split()[1]
    case = [int(c) for c in case]
    print "Case #%d: %d" % (i, calc(case))
    
