import sys

def get_result(case, C, F, X):
    res_str = 'Case #{case}: {time}'

    def get_min_time(cum_time, cum_rate):
        cur_finishing_time = (cum_time + (X / cum_rate))

        cum_time += (C / cum_rate)
        cum_rate += F
        return (cur_finishing_time, cum_time, cum_rate)

    t = sys.maxint
    cur_t = 0
    cum_time = 0
    cum_rate = 2
    while (t > cur_t):
        if cur_t != 0:
            t = cur_t
        cur_t, cum_time, cum_rate = get_min_time(cum_time, cum_rate)

    min_time = t
    min_time_str = '%0.7f' % min_time

    return res_str.format(case=case, time=min_time_str)

def main(argv):
    out = open('out.txt', 'w')
    f = open(argv[0], 'r')
    testcases = int(f.readline())

    for case in xrange(testcases):
        (C, F, X) = [float(x) for x in f.readline().split()]

        res = get_result(case + 1, C, F, X)
        out.write(res + '\n')

    out.close()
    f.close()

if __name__ == "__main__":
   main(sys.argv[1:])