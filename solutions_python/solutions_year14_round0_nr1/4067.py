from pprint import pprint

def parseTestCase(test_case, test_case_number):
    choice1 = int(test_case.readline())
    matrix1 = read_matrix(test_case)

    choice2 = int(test_case.readline())
    matrix2 = read_matrix(test_case)

    row1 = matrix1[choice1 - 1]
    row2 = matrix2[choice2 - 1]

    result = set(row1).intersection(set(row2))

    if len(result) == 0:
        print ("Case #{}: Volunteer cheated!".format(test_case_number))
    elif len(result) == 1:
        print ("Case #{}: {}".format(test_case_number, list(result)[0]))
    else :
        print ("Case #{}: Bad magician!".format(test_case_number))

def read_matrix(file):
    numbers = []
    for i in xrange(1, 5):
        row = test_case.readline()
        row_numbers = row[:-1].split(" ")
        numbers.append(row_numbers)
    return numbers


test_case = open('A-small-attempt0.in')

nb_test_cases = int (test_case.readline())

for i in xrange(1, nb_test_cases + 1):
    parseTestCase(test_case, i)