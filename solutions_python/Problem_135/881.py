input_file = open('input01.txt', 'r')
output_file = open('output01.txt', 'w')

case_number = int(input_file.readline())

for i in range(case_number):
    case = [[], []]
    for j in range(2):
        target = int(input_file.readline())

        for k in range(target - 1):
            input_file.readline()

        case[j] = [int(k) for k in input_file.readline().split()]

        for k in range(4 - target):
            input_file.readline()

    matched_count = 0
    matched_number = 0

    print case
    for j in case[0]:
        if case[1].count(j) != 0:
            matched_count += 1
            matched_number = j

    if matched_count == 1:
        result = str(matched_number)
    elif matched_count == 0:
        result = 'Volunteer cheated!'
    else:
        result = 'Bad magician!'

    output_file.write('Case #' + str(i + 1) + ': ' + result + '\n')
