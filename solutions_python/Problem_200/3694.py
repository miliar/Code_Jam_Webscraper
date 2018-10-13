import sys


def execute(input_str):
    input_str = input_str.strip()
    last_tidy_str = input_str
    for i in range(1, len(input_str)):
        if input_str[i] < input_str[i-1]:
            last_tidy_str = input_str[:i-1] + str(int(input_str[i-1]) - 1) + '9'*(len(input_str)-i)
            return execute(last_tidy_str)
    return last_tidy_str.lstrip('0')

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, 'r') as in_f, open(output_file, 'w') as out_f:
        num_case = int(in_f.readline())
        for i in range(1, num_case+1):
            input = in_f.readline()
            output = execute(input)
            out_f.write('Case #{i}: {output}\n'.format(i=i, output=output))
    print('total number of cases: {} - done.'.format(num_case))