import argparse

def preprocess_data(data_str):
    mapping = {'-': False, '+': True}
    chars, k = data_str.split(' ')
    return int(k), [mapping[char] for char in list(chars)]

def flip_pancakes(state):
    return [not x for x in state]

def count_flips(k, state):
    count = 0
    for ix in xrange(0, len(state)-k+1):
        slice = state[ix:ix+k]

        if not slice[0]:
            state[ix:ix+k] = flip_pancakes(slice)
            count += 1

    return count if all(state) else -1


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

    output = []
    for k, state in cases:
        output.append(count_flips(k, state))

    print output

    with open(output_path, 'w') as fd:
        for ix, count in enumerate(output):
            mapping = {-1: 'IMPOSSIBLE'}
            fd.write('Case #%d: %s\n' % (ix+1, mapping.get(count, count)))
