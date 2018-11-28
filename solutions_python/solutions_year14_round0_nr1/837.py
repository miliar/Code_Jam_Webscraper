import sys


def read_board_state(istream):
    return [
        istream.readline().split(),
        istream.readline().split(),
        istream.readline().split(),
        istream.readline().split()
    ]


def main():
    istream = sys.stdin
    number_of_cases = int(istream.readline())
    for case_no in xrange(1, number_of_cases + 1):
        first_choose = int(istream.readline()) - 1
        first_board = read_board_state(istream)
        second_choose = int(istream.readline()) - 1
        second_board = read_board_state(istream)
        intersection = set(first_board[first_choose]).intersection(
                           second_board[second_choose])
        print 'Case #%d:' % case_no,
        if len(intersection) == 0:
            print 'Volunteer cheated!'
        elif len(intersection) > 1:
            print 'Bad magician!'
        else:
            for x in intersection:
                print x

if __name__ == '__main__':
    main()
