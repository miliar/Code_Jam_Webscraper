import sys


def execute(input_str):
    num_stall = int(input_str.split(' ')[0])
    num_ppl = int(input_str.split(' ')[1])
    array_empty_stall = [num_stall]
    new_left = None
    new_right = None
    for i in range(0, num_ppl):
        longest_empty = max(array_empty_stall)
        longest_empty_index = array_empty_stall.index(longest_empty)
        array_empty_stall.pop(longest_empty_index)
        new_left = int((longest_empty-1)/2)
        new_right = (longest_empty-1) - int((longest_empty-1)/2)
        array_empty_stall.insert(longest_empty_index, new_right)
        array_empty_stall.insert(longest_empty_index, new_left)
    return '{} {}'.format(max(new_left, new_right), min(new_left, new_right))


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