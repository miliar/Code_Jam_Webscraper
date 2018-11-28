str_format = "Case #{0}: {1}\n"
names = ['RICHARD', 'GABRIEL']

with open("D-small-attempt0.in", "r") as input_f:
    first_line = input_f.readline()
    case_number = int(first_line)
    for case_nr in range(case_number):
        # INPUT
        one_line = input_f.readline()
        X, R, C = one_line.split()
        X = int(X)
        R = int(R)
        C = int(C)

        # DO SMTH
        if X >= 7:
            who = 0
        elif R * C % X != 0:
            who = 0
        elif X == 1:
            who = 1
        elif X == 2:
            if max(R, C) >= X and min(R, C) >= (X - 1):
                who = 1
            else:
                who = 0
        elif X == 3:
            if max(R, C) >= X and min(R, C) >= (X - 1):
                who = 1
            else:
                who = 0
        elif X == 4:
            if max(R, C) >= X and min(R, C) >= (X - 1):
                who = 1
            else:
                who = 0
        elif X == 5:
            if max(R, C) >= X and min(R, C) >= (X - 1):
                who = 1
            else:
                who = 0
        elif X == 6:
            if max(R, C) >= X and min(R, C) >= (X - 2):
                who = 1
            else:
                who = 0

        # OUTPUT
        with open('output.txt', 'a') as output_f:
            output_f.write(str_format.format(case_nr + 1, names[who]))
        #print(str_format.format(case_nr + 1, output))
        if one_line == '':
            break
