from sys import stdin

MISTAKE = 'Bad magician!'
CHEAT = 'Volunteer cheated!'

def trick_result(matrix1, answer1, matrix2, answer2):
    row1 = matrix1[answer1 - 1]
    row2 = matrix2[answer2 - 1]
    intersection = set(row1).intersection(row2)

    # detect mistake by checking to see that contents of first chosen row are
    # all in different rows in second arrangement
    if len(intersection) == 1:
        return intersection.pop()

    # detect chosen card by looking for one card that's in both chosen rows
    if len(intersection) == 0:
        return CHEAT

    # if no card satisfies, return cheat
    return MISTAKE


def parse_input(solver):
    num_cases = int(stdin.readline())

    for case in range(1, num_cases + 1):
        answer1 = int(stdin.readline())

        matrix1 = [
            [int(num) for num in stdin.readline().split(' ')]
            for i in range(4)
        ]

        answer2 = int(stdin.readline())

        matrix2 = [
            [int(num) for num in stdin.readline().split(' ')]
            for i in range(4)
        ]

        result = solver(matrix1, answer1, matrix2, answer2)
        print 'Case #%d: %s' % (case, result)

if __name__ == '__main__':
    parse_input(trick_result)
