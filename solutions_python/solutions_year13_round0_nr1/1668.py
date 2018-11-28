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


X = "X won"
O = "O won"
DRAW = "Draw"
NOTCOMPLETED = "Game has not completed"


def skip_remind(stream, counter):
    for _ in range(3-counter):
        stream.readline()


def format_case(case, result):
    return "Case #{0}: {1}\n".format(case, result)


def success_line(line, successor):
    return set(line) in [set([successor, 'T']), set([successor])]


def calculate_winner(infile):
    verticals = [[], [], [], []]
    diagonals = [[], []]
    result = DRAW
    for j in range(4):
        line = infile.readline()
        print "line %d:" % j, line
        line = line.strip()

        if success_line(line, 'X'):
            skip_remind(infile, j)
            return X
        elif success_line(line, 'O'):
            skip_remind(infile, j)
            return O
        for i, node in enumerate(line):
            verticals[i].append(node)
            if node == '.':
                result = NOTCOMPLETED
        print line, j
        print line[j]

        diagonals[0].append(line[j])
        diagonals[1].append(line[3-j])
    for line in verticals:
        if success_line(line, 'X'):
            return X
        elif success_line(line, 'O'):
            return O
    for line in diagonals:
        if success_line(line, 'X'):
            return X
        elif success_line(line, 'O'):
            return O
    return result


def process_file(infile, outfile):
    Cases = int(infile.readline())
    print "We have %d cases." % Cases
    out_str = []
    for case in range(1, Cases+1):
        print "case: %d" % case
        out_str.append(format_case(case, calculate_winner(infile)))
        infile.readline()
        print "embty line"
    for case in out_str:
        outfile.write(case)


if __name__ == '__main__':
    from sys import argv
    process_file(open(argv[1]), open(argv[1].replace(".in", ".out"), "w"))
