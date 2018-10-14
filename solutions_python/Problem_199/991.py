def fliped(data, zero_pos, size):
    flip = {0 : 1, 1 : 0}
    return data[0:zero_pos] + tuple(map(lambda value: flip[value], data[zero_pos: zero_pos + size])) + data[zero_pos+size:]


def solve(data, size):
    result = str(0)
    while(True):
        try:
            zero_pos = data.index(0)
        except ValueError:
            return result
        if zero_pos + size > len(data):
            return 'IMPOSSIBLE'

        data = fliped(data, zero_pos, size)

        result = str(int(result) + 1)


def main():
    input_file_name = 'A-input.in'
    output_file_name = 'A-output.out'
    with open(input_file_name) as fin:
        with open(output_file_name, 'w') as fout:
            t = int(fin.readline())
            for i in range(t):
                raw_data = fin.readline().split()
                mapper = {'+': 1, '-' : 0}
                data = tuple(map(lambda value: mapper[value], raw_data[0]))
                size = int(raw_data[1])
                fout.write("Case #%d: %s\n" % (i+1, solve(data, size)))

main()