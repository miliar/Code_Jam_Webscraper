def get_tidy_pos(n):
    str_n = str(n)
    last = 0
    for idx, c in enumerate(str_n):
        if last > int(c):
            return idx
        last = int(c)

    return -1


def solve(n):
    while n > 0:
        tidy_value = get_tidy_pos(n)
        if tidy_value == -1:
            return n
        else:
            str_n = str(n)
            n = int(str_n[0:tidy_value - 1] + str(int(str_n[tidy_value - 1]) - 1) + ("9" * len(str_n[tidy_value:])))

    return 1


def main():
    input_file_name = 'B-input.in'
    output_file_name = 'B-output.out'
    with open(input_file_name) as fin:
        with open(output_file_name, 'w') as fout:
            t = int(fin.readline())
            for i in range(t):
                n = int(fin.readline())
                fout.write("Case #%d: %d\n" % (i+1, solve(n)))

main()