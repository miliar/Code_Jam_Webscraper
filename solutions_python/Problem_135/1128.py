import sys


def get_trick_results(answer1, answer2, row1, row2):
    """
    Get results for trick

    :param    answer1: first answer
    :type     answer1: int
    :param    answer2: second answer
    :type     answer2: int
    :param    row1:  first selected row
    :type     row1:  list
    :param    row2:  second selected row
    :type     row2:  list

    :returns: trick result
    :rtype:   str
    """
    result = set(row1).intersection(set(row2))
    if len(result) == 1:
        return result.pop()
    elif len(result) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'


def main(argv=sys.argv):

    count = int(sys.stdin.readline())
    for i in range(count):
        answer1 = int(sys.stdin.readline())
        row1 = map(int, (
            sys.stdin.readline(),
            sys.stdin.readline(),
            sys.stdin.readline(),
            sys.stdin.readline()
        )[answer1-1].split(' '))
        answer2 = int(sys.stdin.readline())
        row2 = map(int, (
            sys.stdin.readline(),
            sys.stdin.readline(),
            sys.stdin.readline(),
            sys.stdin.readline()
        )[answer2-1].split(' '))
        sys.stdout.write(
            'Case #{0}: {1}\n'.format(
                i+1,
                get_trick_results(answer1, answer2, row1, row2)
            )
        )
if __name__ == '__main__':
    main()
