import sys

def last_tidy_number(integer_string):
    untidy_ind = None
    tidy_list = list(integer_string)

    for i in xrange(len(tidy_list) - 1, 0, -1):
        current_digit = int(tidy_list[i])
        previous_digit = int(tidy_list[i - 1])
        if current_digit < previous_digit:
            untidy_ind = i - 1
            tidy_list[i - 1] = str(previous_digit - 1)

    if untidy_ind is not None:
        for j in xrange(untidy_ind + 1, len(tidy_list)):
            tidy_list[j] = '9'

    return str(int(''.join(tidy_list)))

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = input_file.split('.')[0] + '_output.txt'
    with open(input_file, 'rb') as f:
        with open(output_file, 'wb') as o:
            T = f.readline()
            for i, line in enumerate(f):
                answer = last_tidy_number(line.rstrip())
                o.write("Case #" + str(i + 1) + ": " + answer + "\n")
