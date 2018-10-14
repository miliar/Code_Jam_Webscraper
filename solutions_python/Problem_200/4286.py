"""
 Created by memduhcagridemir
 08.04.2017
"""


def get_max_tidy(num):
    if len(num) <= 1:
        return num

    num = [int(n) for n in num]

    i = 0
    while i < len(num) - 1:
        tens = num[i]
        ones = num[i + 1]

        if ones >= tens:
            i += 1
            continue

        num[i] -= 1
        for j in range(i + 1, len(num)):
            num[j] = 9

        i = 0

    num = [str(n) for n in num]

    return num

with open('B-large.in') as input_file:
    number_of_inputs = input_file.readline()

    for inp in range(int(number_of_inputs)):
        current_input = input_file.readline().rstrip()
        output = get_max_tidy(list(current_input))

        print "Case #{input_number}: {output}".format(input_number=inp+1, output="".join(output).lstrip("0"))
