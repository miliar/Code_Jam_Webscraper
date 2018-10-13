LINES_FOR_EACH_INPUT = 1
INPUT_FILE_NAME = 'B-large.in'
OUTPUT_FILE_NAME = 'B-large.out'


def do_case(s):
    for i in range(len(s)-1):
        if(int(s[i+1])<int(s[i])):
            p=s.find(s[i])
            temp=s[:p+1]+'0'*(len(s)-p-1)
            return str(int(temp)-1)
    return s


def do_parse(input):
    return [line.rstrip().split(" ") for line in input][0][0]


def main():
    input_f = open(INPUT_FILE_NAME, 'r')
    output = []

    num_of_test_cases = int(input_f.readline(), 10)

    input_lines = input_f.readlines()

    for test_case in range(num_of_test_cases):
        parsed_input = do_parse(input_lines[test_case * LINES_FOR_EACH_INPUT: (test_case + 1) * LINES_FOR_EACH_INPUT])
        output.append('Case #' + str(test_case + 1) + ': ' + do_case(parsed_input))

    output_f = open(OUTPUT_FILE_NAME, 'w')
    output_f.write('\n'.join(output))

    input_f.close()
    output_f.close()


if __name__ == '__main__':
    main()