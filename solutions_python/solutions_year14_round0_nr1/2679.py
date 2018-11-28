import sys


def input_reader(f):
    def _read_table():
        return [[int(x) for x in fh.readline().split()]
                for row in range(0,4)]

    def _read_case():
        a1 = int(fh.readline())
        t1 = _read_table()
        a2 = int(fh.readline())
        t2 = _read_table()
        return a1-1,t1,a2-1,t2

    with open(f, "r") as fh:
        cases = int(fh.readline())
        for caseno in range(1,cases+1):
            yield caseno, _read_case()


def solve_case(a1, t1, a2, t2):
    BADMAG = "Bad magician!"
    CHEAT = "Volunteer cheated!"

    s1 = set(t1[a1])
    s2 = set(t2[a2])

    deduce = s1 & s2
    try:
        card = deduce.pop()
    except KeyError:
        return CHEAT

    if deduce:
        return BADMAG

    #for row in t2:
    #    if len(set(row) & s1) != 1:
    #        return BADMAG

    return card


if __name__ == "__main__":
    if len(sys.argv) > 1:
        infile = sys.argv[1]
    else:
        infile = "/dev/stdin"
    if len(sys.argv) > 2:
        outfile = sys.argv[2]
    else:
        outfile = "/dev/stdout"
    with open(outfile, "w") as ofh:
        for caseno, case in input_reader(infile):
            print >> ofh, "Case #%d:" % caseno,
            print >> ofh, solve_case(*case)
