def tidy_number(input_num):
    input_digit = [int(i) for i in str(input_num)]
    for i in reversed(range(1, len(input_digit))):
        if input_digit[i] < input_digit[i - 1]:
            input_digit[i - 1] -= 1
            for x in range(i, len(input_digit)):
                input_digit[x] = 9
    if input_digit[0] == 0:
        input_digit.remove(input_digit[0])
    input_num = ''.join(map(str, input_digit))
    return input_num


if __name__ == '__main__':
    input_file = open('B-large.in')
    output_file = open('B-large-out.in', 'w')
    lines = [line.rstrip('\n') for line in input_file]
    for i, stack in enumerate(lines):
        if i == 0:
            continue
        else:
            output_file.write("Case #{}: {}\n".format(i, tidy_number(int(stack))))
