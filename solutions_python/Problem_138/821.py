input_file = open('input04.txt', 'r')
output_file = open('output04.txt', 'w')

case_number = int(input_file.readline())

for i in range(case_number):
    input_file.readline()
    case = []
    case_list = []

    for j in range(2):
        case.append([float(j) for j in input_file.readline().split()])
        case[-1].sort(reverse=True)
        print case[-1]

    while case[0] and case[1]:
        if case[0][-1] < case[1][-1]:
            case_list.append(True)
            case[0].pop()
        else:
            case_list.append(False)
            case[1].pop()

    for j in range(len(case[0])):
        case_list.append(True)

    for j in range(len(case[1])):
        case_list.append(False)

    print case_list

    temp = case_list[:]
    stack = []
    count = 0
    while temp:
        current = temp.pop()

        if current:
            stack.append(current)
        elif stack and stack[-1]:
            stack.pop()
            count += 1

    print count

    temp = case_list[::-1]
    stack = []

    while temp:
        current = temp.pop()

        if current:
            stack.append(current)
        elif stack and stack[-1]:
            stack.pop()

    print len(stack)

    output_file.write('Case #' + str(i + 1) + ': ' + str(count) + ' ' + str(len(stack)) + '\n')
