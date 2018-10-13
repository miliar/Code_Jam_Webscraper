import sys


def main():
    import ovation
    args = sys.argv[1:]
    fn = args.pop(0)
    reader = (_.strip().split() for _ in open(fn))
    total_number_tests = int(next(reader)[0])
    for test_case in range(1, total_number_tests+1):
        vals = next(reader)
        max_shyness = int(vals[0])
        shynesses = [int(_) for _ in vals[1]]
        res = ovation.solve_ovation(max_shyness, shynesses, label=test_case)
        print 'Case #%d: %d' % (test_case, res)


if __name__ == '__main__':
    sys.exit(main())
