import sys


def find_possibilities(first_answer, first_matrix,
                       second_answer, second_matrix):
    return set(first_matrix[first_answer - 1]).intersection(
        set(second_matrix[second_answer - 1]))


def possibilities_printer(possibilities):
    if len(possibilities) > 1:
        return 'Bad magician!'
    if len(possibilities) == 0:
        return 'Volunteer cheated!'
    return possibilities.pop()


def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    to_write = []
    for case in range(int(lines[0])):
        c = case * 10
        first_answer = int(lines[c + 1])
        first_matrix = [l.split() for l in lines[c + 2: c + 6]]
        second_answer = int(lines[case * 10 + 6])
        second_matrix = [l.split() for l in lines[c + 7: c + 11]]
        possibilities = find_possibilities(first_answer, first_matrix,
                                           second_answer, second_matrix)
        to_write.append('Case #{}: {}'.format(
            case + 1,
            possibilities_printer(possibilities))
        )

    [print(x) for x in to_write]


if __name__ == '__main__':
    main()
