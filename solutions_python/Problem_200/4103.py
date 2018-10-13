input_file = open('input.txt')
int_list = []

for line in range(int(input_file.readline())):
    temp_str = input_file.readline() # To
    int_list.append(temp_str.strip())

case_count = 0
for int_str in int_list[:]:
    case_count += 1
    digits = len(int_str)  # Digit Counter
    # Go through the integer string and decrement the largest.
    for index in range(digits - 1):
        digits -= 1
        if int(int_str[index]) > int(int_str[index + 1]):
            biggest = int(int_str[index])
            rep_index = int_str.index(str(biggest))
            more_digits = int_str.count(str(biggest)) - 1
            if biggest == 0 and index > 0:
                biggest = 9
            else:
                biggest -= 1
            int_str = int_str[:rep_index] + str(biggest) + '9'*(digits+more_digits)
            break
    print('Case #{}: {}'.format(case_count, int(int_str)))