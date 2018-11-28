import sys

def handle_case(infile):
    line = [float(x) for x in infile.readline().split()]
    c, f, x = line

    time = 0.0
    farms = 0.0
    best = float("inf")
    while True:
        cps = 2.0 + f*farms
        finish_time = compute_time(cps, x, time)

        # time to buy next farm
        time = time + c/cps
        farms = farms + 1

        if finish_time < best:
            best = finish_time
        else:
            return best

# always have 0 cookies when a farm is built
def compute_time(cps, x, time):
    return time + x/cps



infile = open(sys.argv[1])
cases = int(infile.readline().strip())

for i in xrange(cases):
    print "Case #%d: %f"%(i + 1, handle_case(infile))
