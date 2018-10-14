

def magic(case, first_ans, second_ans, first_square, second_square):
    first_line = first_square[first_ans - 1]
    second_line = second_square[second_ans - 1]

    ans = -1
    counter = 0

    for number in first_line:
        if number in second_line:
            counter += 1
            ans = number

    if counter == 1:
        print_result(case, 1, ans)
    elif counter > 1:
        print_result(case, 2, 0)
    elif counter == 0:
        print_result(case, 3, 0)



def print_result(case, result, line_num):
    if result == 1:
        print ("Case #" + str(case) + ": " + str(line_num))
    elif result == 2:
        print ("Case #" + str(case) + ": " + "Bad magician!")
    elif result == 3:
        print ("Case #" + str(case) + ": " + "Volunteer cheated!")


file_name = "A-small-attempt1.in"

with open(file_name) as f:
    case_num = int(f.readline())
    for i in range(1, case_num + 1):
        first_ans = int(f.readline())
        first_square = []
        first_square.append(f.readline().strip().split(' '))
        first_square.append(f.readline().strip().split(' '))
        first_square.append(f.readline().strip().split(' '))
        first_square.append(f.readline().strip().split(' '))
        second_ans = int(f.readline())
        second_square = []
        second_square.append(f.readline().strip().split(' '))
        second_square.append(f.readline().strip().split(' '))
        second_square.append(f.readline().strip().split(' '))
        second_square.append(f.readline().strip().split(' '))
        magic(i, first_ans, second_ans, first_square, second_square)
