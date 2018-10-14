import sys


def solve(D, N, cases):
    # print(D, N, cases)
    max_time = 0
    for c in cases:
        curr_time = (D - c[0]) / c[1]
        if curr_time > max_time:
            max_time = curr_time
    res = D / max_time
    return res


def process_file(input_file, output_file):
    file_in = open(input_file, 'rU')
    file_out = open(output_file, 'w')

    num_cases = None
    case_num = 0

    cases = []
    D = None
    N = None

    for row in file_in:
        # print(row)

        if not num_cases:
            num_cases = int(row)

        elif D is None:
            case_num += 1
            row_split = row.split()
            D = int(row_split[0])
            N = int(row_split[1])
            cases = []

        elif len(cases) < N:
            row_split = row.split()
            cases.append((int(row_split[0]), int(row_split[1])))

        if len(cases) == N:
            # print('Case %i' % case_num)
            result = solve(D, N, cases)
            res_string = 'Case #%i: %.7f' % (case_num, result)
            # print(res_string)
            file_out.write(res_string + '\n')
            D = None
            N = None
            cases = []


    file_out.close()


def main():
    if len(sys.argv) == 3:
        print('Program starts')
        process_file(sys.argv[1], sys.argv[2])
        print('Done')
        sys.exit(1)

    else:
        print('Give two arguments (INPUT_FILE OUTPUT_FILE)')
        sys.exit(1)


if __name__ == '__main__':
    main()
