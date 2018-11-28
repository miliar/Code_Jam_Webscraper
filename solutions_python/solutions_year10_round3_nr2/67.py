#!/opt/local/bin/python3.1
import sys
import math

def test_count(lower, upper, factor):
    n = math.ceil(math.log(upper / lower, factor))
    m = math.ceil(math.log(n, 2))
    return m

def main(argv=None):
    if not argv:
        argv = sys.argv

    infile = open(argv[1], 'r')
    outfile = open(argv[2], 'w')

    n_testcases = int(infile.readline())
    count = 0

    for line in infile:
        count += 1
        lower, upper, factor = [int(n) for n in line.split()]

        print('Case #{0}: {1}'.format(count, test_count(lower, upper, factor)), file=outfile)

    if not n_testcases == count:
        print('{0} lines left. something wrong with the input file'.format(n_testcases - count))

if __name__ == '__main__':
    sys.exit(main())
