__author__ = 'danolsen'

bad = 'Bad magician!'
cheat = 'Volunteer cheated!'

with open('input/one.txt') as f:
    cases = int(f.readline())

    with open('output/one.txt', 'w') as out:
        for i in range(1, cases+1):
            answer_one = int(f.readline())
            # print answer_one

            line_one = f.readline().split()
            line_two = f.readline().split()
            line_three = f.readline().split()
            line_four = f.readline().split()

            first_line = None
            if answer_one == 1:
                first_line = line_one
            elif answer_one == 2:
                first_line = line_two
            elif answer_one == 3:
                first_line = line_three
            elif answer_one == 4:
                first_line = line_four

            # print first_line

            answer_two = int(f.readline())

            # print answer_two

            line_one = f.readline().split()
            line_two = f.readline().split()
            line_three = f.readline().split()
            line_four = f.readline().split()

            second_line = None
            if answer_two == 1:
                second_line = line_one
            elif answer_two == 2:
                second_line = line_two
            elif answer_two == 3:
                second_line = line_three
            elif answer_two == 4:
                second_line = line_four

            # print second_line

            third_line = list(set(first_line) & set(second_line))
            # print third_line
            if len(third_line) == 1:
                out.write('Case #%d: %s\n' % (i, third_line[0]))
            elif len(third_line) == 0:
                out.write('Case #%d: %s\n' % (i, cheat))
            else:
                out.write('Case #%d: %s\n' % (i, bad))

            # print len(third_line)
