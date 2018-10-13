#!/opt/local/bin/python3.1
import sys

def next(num, modulo):
    return (num + 1) % modulo

def calc_profit(times, size, groups):
    if size >= sum(groups):
        return times * sum(groups)
    profit = 0
    index = 0
    passenger = 0
    for i in range(times):
        passenger += groups[index]
        while passenger <= size:
            index = next(index, len(groups))
            passenger += groups[index]
        profit += passenger - groups[index]
        passenger = 0
    return profit

def main(argv=None):
    if not argv:
        argv = sys.argv

    infile = open(argv[1], 'r')
    outfile = open(argv[2], 'w')

    n_testcases = int(infile.readline())
    count = 0

    for line in infile:
        count += 1
        times, size, n_groups = [int(n) for n in line.split()]
        groups = [int(n) for n in infile.readline().split()]
        if not len(groups) == n_groups:
            print('invalid testcase in {0}-th line\nskip this case'.format(count + 1))
            continue

        print('Case #{0}: {1}'.format(count, calc_profit(times, size, groups)), file=outfile)

    if not n_testcases == count:
        print('{0} lines left. something wrong with the input file'.format(n_testcases - count))

if __name__ == '__main__':
    sys.exit(main())
