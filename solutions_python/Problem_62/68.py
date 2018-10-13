#!/opt/local/bin/python3.1
import sys

def count_intersect(ropes):
    print(ropes)
    res = 0
    ropes.sort()
    for rope in ropes:
        for other in ropes:
            if rope[0] < other[0] and rope[1] > other[1]:
                res += 1
    return res

def main(argv=None):
    if not argv:
        argv = sys.argv

    infile = open(argv[1], 'r')
    outfile = open(argv[2], 'w')

    n_testcases = int(infile.readline())
    count = 0

    for line in infile:
        count += 1
        n_ropes = int(line)

        ropes = []
        for i in range(n_ropes):
            ropes.append([int(n) for n in infile.readline()[:-1].split()])

        print('Case #{0}: {1}'.format(count, count_intersect(ropes)), file=outfile)

    if not n_testcases == count:
        print('{0} lines left. something wrong with the input file'.format(n_testcases - count))

if __name__ == '__main__':
    sys.exit(main())
