import sys

def when(goal, start, rate):
    return (goal/rate) + start

t = int(sys.stdin.readline())



for case in range(1, t + 1):
    rate = 2.0
    start = 0.0
    params = sys.stdin.readline().split()
    c = float(params[0])
    f = float(params[1])
    x = float(params[2])
    while 1:
        
        timeAtCurrentRate = when(x, start, rate)
        whenNextFactory = when(c, start, rate)
        timeWithNextFactory = when(x, whenNextFactory, rate + f)

        if timeAtCurrentRate <= timeWithNextFactory:
            break;

        start = whenNextFactory
        rate += f

    print "Case #%d: %02.7f" % (case, timeAtCurrentRate)
