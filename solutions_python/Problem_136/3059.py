import sys


def should_buy_farm(c, f, x, cur_rate):
    time_to_farm = c / cur_rate
    time_to_end = x / cur_rate
    time_to_end_and_farm = x / (cur_rate + f)
    return time_to_farm + time_to_end_and_farm < time_to_end

def run_test(line):
    split = line.split()
    c = float(split[0])
    f = float(split[1])
    x = float(split[2])
    cur_rate = 2.0
    time = 0.0
    while True:
        if should_buy_farm(c, f, x, cur_rate):
            time += c / cur_rate
            cur_rate += f
        else:
            return time + x / cur_rate



def main():
    filename = sys.argv[1]
    with open(filename) as f:
        tests = int(f.readline())
        for i in range(tests):
            result = run_test(f.readline())
            print "Case #%d: %.7f" % (i + 1, result)

if __name__ == '__main__':
    main()
