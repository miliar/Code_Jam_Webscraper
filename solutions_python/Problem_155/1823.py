str_format = "Case #{0}: {1}\n"

with open("A-large.in", "r") as input_f:
    first_line = input_f.readline()
    case_number = int(first_line)
    for case_nr in range(case_number):
        # INPUT
        one_line = input_f.readline()

        # DO SMTH
        s_max, s_string = one_line.split()
        # len(s_string) = s_max + 1
        s_max = int(s_max)
        s_list = list(s_string)
        output = 0
        total_standing = 0
        for current_s in range(s_max + 1):
            diff = current_s - total_standing # <= 0
            if diff <= 0:
                total_standing += int(s_list[current_s])
            else:
                output += diff
                total_standing += int(s_list[current_s]) + diff

        # OUTPUT
        with open('output.txt', 'a') as output_f:
            output_f.write(str_format.format(case_nr + 1, output))
        #print(str_format.format(case_nr + 1, output))
        if one_line == '':
            break
