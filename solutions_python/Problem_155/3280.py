__author__ = 'gaby'

out_file = open('output.out.txt', 'w+')
in_file = open('A-large.in', 'r+')
num_cases = int(in_file.readline())

for c in range(0, num_cases):
    line = in_file.readline().strip('\n').split()

    max_shyness_level = int(line[0]) + 1
    shyness_level_settings = list(line[1])

    up = 0
    friends = 0

    for l in range(0, max_shyness_level):
        if int(shyness_level_settings[l]) != 0:
            if up < l:
                plus = l - up
                friends += plus
                up += plus

            up += int(shyness_level_settings[l])

    case = 'Case #' + str(c + 1) + ': ' + str(friends)
    out_file.write(case + '\n')
