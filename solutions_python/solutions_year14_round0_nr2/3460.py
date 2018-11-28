import sys

infile = sys.argv[1]

def get_farm_time(n, c, f, x):
    return sum(((c*1.0)/(2.0+i*f) for i in xrange(n)))+(x*1.0)/(2.0+n*f)
        

def format_out(case, t):
    print "Case #%d: %0.7f" % (case,t)

with open(infile) as in_fp:
    num_tcs = int(in_fp.readline())
    for t in range(1,1+num_tcs):
        fields = map(lambda j: float(j), in_fp.readline().split())
        c,f,x = fields[0],fields[1],fields[2]
        if c>x:
            format_out(t,x/2.0)
            continue
        this_time = -1
        prev_time = -1
        numfarms = 0
        while True:
            this_time = get_farm_time(numfarms, c,f,x)
            if (prev_time != -1 and this_time > prev_time):
                format_out(t, prev_time)
                break
            numfarms += 1
            prev_time = this_time
