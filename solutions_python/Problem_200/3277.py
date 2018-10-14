input_file = open('B-large.in', 'r')
input = input_file.readlines()
input_file.close()

n = input[0]
lines = input[1:]
index = 1
output_lines = []
for number in lines:
    number = number.strip()
    number_length = len(number) - 1

    for i in range(number_length + 1):

        current_number_index = number_length - i
        if i < number_length:

            before_number_index = number_length - i - 1

            if int(number[current_number_index]) < int(number[before_number_index]):
                number = number[: before_number_index] + str(int(number[before_number_index]) - 1) + '9' * (i + 1)

        elif int(number[current_number_index]) == 0:
            number = number[1:]

    output_lines.append("Case #" + str(index) + ": " + number + "\n")
    index += 1

output_file = open('ouput', 'w')
output_file.writelines(output_lines)
output_file.close()

