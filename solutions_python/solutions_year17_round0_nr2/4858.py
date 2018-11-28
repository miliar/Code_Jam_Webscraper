"""
Finds the last tidy number in a sequence
"""

def last_tidy_num():
    """Finds the last tidy number in a sequence"""
    with open("B-small-attempt2.in", "r") as in_file, open("output.txt", "w") as out_file:
        next(in_file)
        case_num = 1
        for line in in_file:
            current_num = int(line.strip())
            if current_num % 10 == 0 and str(current_num).startswith('1'):
                digit_count = len([d for d in str(current_num)]) - 1
                last_tidy = ''
                for _ in range(digit_count):
                    last_tidy += '9'
                to_write = 'Case #' + str(case_num) + ': ' + str(last_tidy) + '\n'
                case_num += 1
                out_file.write(to_write)
                print(last_tidy)
            elif current_num < 10:
                to_write = 'Case #' + str(case_num) + ': ' + str(current_num) + '\n'
                out_file.write(to_write)
                case_num += 1
                print(current_num)
            else:
                for num in range(current_num, 0, -1):
                    if num == int(sort_and_digitize(num)):
                        to_write = 'Case #' + str(case_num) + ': ' + str(num) + '\n'
                        out_file.write(to_write)
                        case_num += 1
                        print(num)
                        break

def sort_and_digitize(line):
    """sorts the digits within number and return as integer"""
    return int(''.join(sorted(str(line))))

last_tidy_num()
