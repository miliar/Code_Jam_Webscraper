INPUT_FILE = 'magic_test.in'
OUTPUT_FILE = 'magic_test.out'

BAD = 'Bad magician!'
CHEAT = 'Volunteer cheated!'

in_file = open(INPUT_FILE, 'r')
out_file = open(OUTPUT_FILE, 'w')

n = int(in_file.readline())
case = 1

while n > 0:
    out_file.write('Case #' + str(case) + ': ')

    first_answer = int(in_file.readline())

    i = 1
    first_row = in_file.readline()
    while i < first_answer:
        first_row = in_file.readline()
        i += 1

    while i < 4:
        in_file.readline()
        i+= 1

    second_answer = int(in_file.readline())
    i = 1
    second_row = in_file.readline()
    while i < second_answer:
        second_row = in_file.readline()
        i += 1

    first_row = first_row.split()
    second_row = second_row.split()
    print first_row
    print second_row

    find_count = 0
    found_card = ''
    for c in first_row:
        if c in second_row:
            find_count += 1
            # print find_count
            found_card = c
    print find_count, found_card

    if find_count == 0:
        out_file.write(CHEAT)
    elif find_count == 1:
        out_file.write(found_card)
    elif find_count > 1:
        out_file.write(BAD)

    out_file.write('\n')

    while i < 4:
        in_file.readline()
        i+= 1

    n -= 1
    case += 1

