import itertools
inputfile = file("B-large.in", "rb")
outputfile = file("B-large.out", "wb")
out_s = "Case #%d: %.7f"
parse_line = lambda: [float(a) for a in inputfile.readline().split()]

T = int(inputfile.readline())

def minimum(r, c, f, x):
    cur_sum = X/r
    for nums in itertools.count(1):
        last_sum = cur_sum
        cur_sum = cur_sum - x/(r + (nums-1)*f) + c/(r+(nums-1)*f) + x/(r + nums*f)
        if cur_sum > last_sum:
            return last_sum
        

for ncase in xrange(1,T+1):
    C, F, X = parse_line()
    print >>outputfile, out_s % (ncase, minimum(2, C, F, X))