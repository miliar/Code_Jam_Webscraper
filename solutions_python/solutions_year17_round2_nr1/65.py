LINES_PARAM = 1
INPUT_FILE_NAME = 'A-large.in'
OUTPUT_FILE_NAME = 'A-large.out'

def arrival(horse,d):
    dist=d-horse[0]
    return dist/horse[1]
def do_case(parsed):
    time=max([arrival(horse,parsed[0][0]) for horse in parsed[1:]])
    return str(parsed[0][0]/time)


def do_parse(input):
    return [[float(num) for num in line.rstrip().split(" ")]for line in input]


def main():
    input_f = open(INPUT_FILE_NAME, 'r')
    output = []

    num_of_test_cases = int(input_f.readline(), 10)
    temp = input_f.readlines()
    index = 0
    for test_case in range(num_of_test_cases):
        lines = int(temp[index].rstrip().split(" ")[LINES_PARAM])
        parsed_input = do_parse(temp[index:index + lines + 1])
        index = index + 1 + lines
        output.append('Case #' + str(test_case + 1) + ': ' + do_case(parsed_input))

    output_f = open(OUTPUT_FILE_NAME, 'w')
    output_f.write('\n'.join(output))

    input_f.close()
    output_f.close()


if __name__ == '__main__':
    main()
