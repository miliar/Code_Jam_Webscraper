__author__ = 'Mohamed'

import math


writer_file = open("output.txt", 'w')

with open("progress_pie_example_input.txt", "r") as reader:
    case = -1
    for number in reader:
        number = number.strip()
        case += 1
        if case == 0:
            continue
        else:
            while True:
                ascending = "".join(sorted(number))
                if ascending == number:
                    break
                number = str(int(number) - 1)
            output = "Case #" + str(case) + ": " + number
            print(output)
            writer_file.write(output+"\n")
    writer_file.close()