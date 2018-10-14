import sys


def calc(line):
    line = line.strip().split()
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])

    rate = 2.0
    curr_time = 0.0
    next_time = 0.0
    total_time = 0.0
    #print x/rate
    while curr_time >= next_time:
        curr_time = x / rate
        next_time = (x / (rate + f)) + (c / rate)
        if curr_time >= next_time:
            total_time += c / rate
        else:
            total_time += curr_time
        rate += f

    return total_time


def main(f):
    test_cases = int(f[0])
    for case in range(test_cases):
        val = calc(f[case + 1])
        print "Case #%d: %.7f" % (case + 1, val)


if __name__ == "__main__":
    f = list(open(sys.argv[1]))
    main(f)