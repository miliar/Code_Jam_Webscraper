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


YES = "YES"
NO = "NO"


def skip_remind(stream, lines, counter):
    for _ in range(lines-counter):
        stream.readline()


def format_case(case, result):
    return "Case #{0}: {1}\n".format(case, result)


def calculate_successor_line(line):
    return len(set(line)) == 1


def case_success(horisontal, vertical):
    for i, line in enumerate(horisontal):
        if calculate_successor_line(line):
            continue
        for j, node in enumerate(line):
            if node == '1':
                if not calculate_successor_line(vertical[j]):
                    return False

    return True


def calculate_case(fin):
    n, m = map(int, fin.readline().strip().split())
    # print n, m
    # print vertical
    if n == 1:
        skip_remind(fin, 1, 0)
        return YES
    vertical = [[] for _ in range(m)]
    lines = []
    for i in range(n):
        line = fin.readline().strip().split()
        lines.append(line)
        for j, node in enumerate(line):
            # print j, node
            vertical[j].append(node)
    if case_success(lines, vertical):
        return YES
    return NO


def process_file(infile, outfile):
    Cases = int(infile.readline())
    print "We have %d cases." % Cases
    out_str = []
    for case in range(1, Cases+1):
        print "case: %d" % case
        out_str.append(format_case(case, calculate_case(infile)))
    for case in out_str:
        outfile.write(case)


if __name__ == '__main__':
    from sys import argv
    process_file(open(argv[1]), open(argv[1].replace(".in", ".out"), "w"))
