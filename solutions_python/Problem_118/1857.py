from math import sqrt

def debug(*args):
    print " ".join(str(arg) for arg in args)


def memoizing(func):
    """Function decorator to cache a function's output."""
    memos = dict()

    def memoize(*args):
        if args in memos:
            return memos[args]
        res = func(*args)
        memos[args] = res
        return res
    return memoize


def format_case(case, result):
    return "Case #{0}: {1}\n".format(case, result)


def is_palendrom(s):
    return len(s) > 0 and s == s[::-1]


def calculate_case(line):
    start, end = map(int, line.split())
    result = 0
    for test in range(start, end+1):
        if is_palendrom(str(test)):
            squarroot = sqrt(test)
            if int(squarroot) != squarroot:
                continue
            if is_palendrom(str(int(squarroot))):
                print test, squarroot
                result += 1
    return result


def process_file(infile, outfile):
    Cases = int(infile.readline())
    print "We have %d cases." % Cases
    out_str = []
    for case in range(1, Cases+1):
        print "case: %d" % case
        out_str.append(format_case(case, calculate_case(infile.readline())))
    for case in out_str:
        outfile.write(case)


if __name__ == '__main__':
    from sys import argv
    process_file(open(argv[1]), open(argv[1].replace(".in", ".out"), "w"))
