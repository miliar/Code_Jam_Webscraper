f = open('input.txt')

count = int(f.readline())

range_four = range(4)

for i in range(count):
    first_guess = int(f.readline())
    for row in range_four:
        row_content = f.readline()
        if row == first_guess - 1:
            first_guessed_row = row_content.split()
    # print first_guessed_row

    second_guess = int(f.readline())
    for row in range_four:
        row_content = f.readline()
        if row == second_guess - 1:
            second_guessed_row = row_content.split()

    common = set(first_guessed_row).intersection(second_guessed_row)
    common_length = len(common)

    case = 'Case #{0}:'.format(i+1)
    if common_length == 1:
        print case, common.pop()
    elif common_length == 0:
        print case, 'Volunteer cheated!'
    else:
        print case, 'Bad magician!'

    # print second_guessed_row
