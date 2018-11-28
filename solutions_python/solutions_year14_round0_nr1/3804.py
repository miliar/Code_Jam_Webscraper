__author__ = 'kesavsundar'

# For each test case, have each row a set for two questions
# Algorithm:
# Answer 1: -> Set_1()
# Answer 2: -> Set_2()
# if Set1 - Set2 == null set
#   User cheated
# if (Set1 intersection Set2).length > 1
#   Magician Magician
# if (Set1 intersection Set2).length == 1
#   Number is the number in set!!!

output_file = open('/home/kesavsundar/googlecodejam/magic_trick/magic_trick_output.txt', 'w')
with open("/home/kesavsundar/googlecodejam/magic_trick/A-small-attempt0.in", 'rb') as test_cases_input:
    test_cases = [line.strip() for line in test_cases_input]
    number_of_test_cases = int(test_cases[0])
    for i in range(0, number_of_test_cases):
        case_start = ((10 * i) + 1)
        case_end = ((10 * i) + 10)
        answer = list()
        rows = list()
        case_input = case_start
        while case_input < case_end:
            answer.append(int(test_cases[case_input]))
            count = 1
            while count <= 4:
                case_input += 1
                rows.append(test_cases[case_input].split(' '))
                count += 1
            case_input += 1

        set_1 = set(rows[answer[0]-1])
        set_2 = set(rows[answer[1]+3])
        magic_answer = set_1.intersection(set_2)
        if len(magic_answer) == 0:
            output_file.write("Case #%s: Volunteer cheated!\n" % (i+1))
        elif len(magic_answer) > 1:
            output_file.write("Case #%s: Bad magician!\n" % (i+1))
        else:
            output_file.write("Case #%s: %s\n" % ((i+1), magic_answer.pop()))


