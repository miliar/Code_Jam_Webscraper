import argparse

def preprocess_data(data_str):
    data = int(data_str)
    digits = []
    while data > 0:
        digit, data = data%10, data/10
        digits.append(digit)
    return digits[::-1]

def find_tidy(last_num):
    changed = [False]*len(last_num)
    for start_ix in xrange(0, len(last_num)):
        for ptr in xrange(len(last_num)-1, start_ix, -1):
            if last_num[ptr] < last_num[ptr-1]:
                last_num[ptr] = 9
                changed[ptr] = True
                if not changed[ptr-1]:
                    last_num[ptr-1] -= 1
    return last_num


if __name__ == '__main__':
    # parse input args
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--input', required=True, help='Path to input file')
    ap.add_argument('-o', '--output', required=True, help='Path to output file')
    args = vars(ap.parse_args())

    input_path = args['input']
    output_path = args['output']

    with open(input_path) as fd:
        num_cases = int(fd.readline().strip())
        cases = [preprocess_data(line.strip()) for line in fd]
    print cases

    output = []
    for last_num in cases:
        last_tidy_list = find_tidy(last_num)
        last_tidy = int(''.join([str(x) for x in last_tidy_list]))
        output.append(last_tidy)

    print 'Output:', output
    with open(output_path, 'w') as fd:
        for ix, last_tidy in enumerate(output):
            fd.write('Case #%d: %s\n' % (ix+1, last_tidy))
