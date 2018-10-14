#!/opt/local/bin/python3.1
import sys

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def multi_gcd(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    d = nums[0]
    for i in range(len(nums) - 1):
        d = gcd(d, nums[i+1])
    return d

def make_prophecy(data):
    diff = [abs(data[i+1] - data[i]) for i in range(len(data)-1)]
    d = multi_gcd(diff)
    return -data[0] % d

def main(argv=None):
    if not argv:
        argv = sys.argv

    infile = open(argv[1], 'r')
    outfile = open(argv[2], 'w')

    n_testcases = int(infile.readline())
    count = 0

    for line in infile:
        count += 1
        raw_data = [int(n) for n in line.split()]
        if not len(raw_data) == raw_data[0] + 1:
            print('invalid testcase in {0}-th line\nskip this case'.format(count + 1))
            continue

        print('Case #{0}: {1}'.format(count, make_prophecy(raw_data[1:])), file=outfile)

    if not n_testcases == count:
        print('{0} lines left. something wrong with the input file'.format(n_testcases - count))

if __name__ == '__main__':
    sys.exit(main())
