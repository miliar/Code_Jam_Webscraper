import sys
sys.setrecursionlimit(2000)
LINES_FOR_EACH_INPUT = 1
INPUT_FILE_NAME = 'A-large.in'#'sample.in'#'A-small-attempt0.in'
OUTPUT_FILE_NAME ='A-large.out'#'sample.out' #'A-small-attempt0.out'
def flip(s,k):
    s[:k]=[not t for t in s[:k]]
def flips(s,k):
    if(len(s)<k):
        if sum(s)!=0:
            return -float('Inf')
        else:
            return 0
    if s[0]==True:
        flip(s,k)
        return flips(s[1:],k)+1
    else:
        return flips(s[1:],k)
def do_case(parsed_input):
    parsed_input=parsed_input[0]
    results=flips([c=='-' for c in parsed_input[0]],int(parsed_input[1]))
    if(results==-float('Inf')):
        return 'IMPOSSIBLE'
    return str(results)


def do_parse(input):
    return [line.rstrip().split(" ") for line in input]


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