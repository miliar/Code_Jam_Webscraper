import sys


def get_row_number(f):
    return int(f.readline().strip())


def get_row(f, r):
    row = []
    for i in range(1, 5):
        c_row = [int(v) for v in f.readline().strip().split(" ")]
        if i == r:
            row = c_row
    return row


def solve(row1, row2):
    r1 = set(row1)
    r2 = set(row2)
    intersection = r1.intersection(r2)
    if not intersection:
        return "Volunteer cheated!"
    elif len(intersection) == 1:
        return intersection.pop()
    elif len(intersection) > 1:
        return "Bad magician!"


def main(filename):
    with open(filename, "r") as f:
        T = int(f.readline().strip())
        for t in xrange(T):
            r = get_row_number(f)
            row1 = get_row(f, r)
            r = get_row_number(f)
            row2 = get_row(f, r)
            result = solve(row1, row2)
            print "Case #%d: %s" % (t+1, result)


if __name__ == "__main__":
    main(sys.argv[1])
