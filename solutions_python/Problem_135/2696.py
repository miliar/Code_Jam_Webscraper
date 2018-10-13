import sys

fileName = sys.argv[1]
inputFile = open(fileName, 'r')
num_cases = int(inputFile.readline())

for test_case_num in range(1, num_cases + 1):

    row_in_first = int(inputFile.readline())

    first_arrangement = []
    second_arrangement = []

    for i in range(0,4):
        first_arrangement.append([int(x) for x in inputFile.readline().split(" ")])
    row_in_second = int(inputFile.readline())
    for i in range(0,4):
        second_arrangement.append([int(x) for x in inputFile.readline().split(" ")])

    candidate_nums_1 = first_arrangement[row_in_first - 1]
    candidate_nums_2 = second_arrangement[row_in_second - 1]

    potential_answers = [x for x in candidate_nums_2 if (x in candidate_nums_1)]

    if len(potential_answers) == 0:
        case_message = "Volunteer cheated!"
    elif len(potential_answers) == 1:
        case_message = potential_answers[0]
    else:
        case_message = "Bad magician!"
    
    print ("Case #{0}: {1}".format(test_case_num, case_message))

inputFile.close()
