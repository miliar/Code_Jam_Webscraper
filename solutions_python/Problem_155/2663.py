import sys


def solve(i, test):
    test = test.split()
    total = 0
    missing = 0
    for si, el in enumerate(test[1]):
        if si > total:
            missing += si - total
            total += si - total
        total += int(el)
    return 'Case #%s: %d' % (i+1, missing)


def main():
    test_file = open(sys.argv[1], 'r')
    res_file = open('results', 'w')
    for i in range(int(test_file.readline())):
        res = solve(i, test_file.readline())
        print res
        res_file.write('%s\n' % res)

    test_file.close()
    res_file.close()


if __name__ == '__main__':
    main()
