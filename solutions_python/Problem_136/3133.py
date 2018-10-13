import sys

if len(sys.argv) != 2:
    raise RuntimeError("usage: cookie.py input")


def min_time(rate, cost, f, goal):
    time = 0
    while True:
        if (goal / rate) < (cost / rate + goal / (rate + f)):
            return time + (goal / rate)
        time += cost / rate
        rate += f


with open(sys.argv[1], 'r') as input_file:
    num_tests = int(next(input_file).strip())
    for t in range(1, num_tests + 1):
        (c, f, x) = (float(x) for x in next(input_file).strip().split())
        result = min_time(2, c, f, x)
        print "Case #%d: %f" % (t, result)