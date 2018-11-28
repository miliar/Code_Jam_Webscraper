def main():
    input_file = open('B-small-attempt3.in', 'r')
    in_string = input_file.read()
    sample_input = filter(bool, in_string.split('\n'))
    sample_input = map(int, sample_input)
    sample_input.pop(0)
    output = ""
    for case_num, case in enumerate(sample_input):
        current = case
        end = str(tidy(current))
        output += "Case #{0}: {1}\n".format(case_num + 1, end)

    output_file = open('out.out', 'w')
    output_file.write(output)

def tidy(num):
    if len(str(num)) == 1:
        return num
    else:
        tidy_num = ''
        if str(num) == ''.join(sorted(str(num))):
            tidy_num = str(num)
        else:
            for index, digit in enumerate(str(num)):
                next_num = index + 1
                if next_num < len(str(num)):
                    if int(digit) >= int(str(num)[next_num]) and int(str(digit)) > int(min(str(num))):
                        sub_num = str(num)[index : len(str(num))]
                        int_sub_num = int(sub_num)
                        partial = int_sub_num - (int_sub_num % pow(10, len(sub_num) - 1) + 1)
                        tidy_num += str(partial)
                        break
                    else:
                        tidy_num += digit
                else:
                    return num
        return tidy_num

main()
