import sys


def solve(c,f,x):
    s = 2.0
    te = 0.0
    nothing = x/s
    while (1):
        farm = (c/s)+(x/(s+f))+te
        if farm > nothing:
            return nothing
        else:
            te = (c/s)+te
            nothing = farm
            s = s+f


if len(sys.argv) > 1:
    filename = sys.argv[len(sys.argv)-1]
else:
    raise Exception("Missing file paramenter")


f = open(filename, 'r')
n = int(f.readline().strip())

for line_no in xrange(0, n):
    cfx = [float(t) for t in f.readline().strip().split()]
    ans = solve(cfx[0], cfx[1], cfx[2])
    case = line_no + 1
    print "Case #{}: {}".format(case, ans)
