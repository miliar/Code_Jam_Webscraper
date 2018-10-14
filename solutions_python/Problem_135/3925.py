def get_matrix():
    matrix = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    for row in range(4):
        line = raw_input()
        matrix[row] = line.split()

    return matrix


def find_number(first, second):
    found_numbers = list()
    for index in first:
        if index in second:
            found_numbers.append(index)
    return found_numbers


if __name__ == '__main__':
    number_of_tests = input()

    for test in range(1, number_of_tests + 1):
        first_volunteer_answer = input()
        first_matrix = get_matrix()
        first_answer = first_matrix[first_volunteer_answer - 1]

        second_volunteer_answer = input()
        second_matrix = get_matrix()
        second_answer = second_matrix[second_volunteer_answer - 1]

        rows = find_number(first_answer, second_answer)

        if len(rows) == 0:
            print "Case #{0}: Volunteer cheated!".format(test)

        elif len(rows) == 1:
            print "Case #{0}: {1}".format(test, rows[0])

        else:
            print "Case #{0}: Bad magician!".format(test)
