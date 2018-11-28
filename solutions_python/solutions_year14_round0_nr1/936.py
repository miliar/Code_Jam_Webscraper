import sys


def read_m_take_nth(fh, m, n):
    line_to_keep = None
    for row in xrange(1, m + 1):
        line = fh.readline()
        if row == n:
            line_to_keep = line
    return line_to_keep


def main():
    fh = sys.stdin
    for test_number in xrange(1, int(fh.readline().strip()) + 1):
        row_num = int(fh.readline().strip())
        nth_row = read_m_take_nth(fh, 4, row_num)
        row_set = set(nth_row.strip().split())
        row_num = int(fh.readline().strip())
        nth_row = read_m_take_nth(fh, 4, row_num)
        matching = row_set.intersection(nth_row.strip().split())
        print "Case #%d:" % (test_number, ),
        if len(matching) == 1:
            print matching.pop()
        elif len(matching) == 0:
            print "Volunteer cheated!"
        else:
            print "Bad magician!"


if __name__ == "__main__":
    main()
