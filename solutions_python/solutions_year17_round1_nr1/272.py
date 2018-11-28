
def run_case(input):
    rows, cols = read_ints(input, 2)
    cake = []
    for row in range(rows):
        col = []
        col_str, = read_strs(input)
        col.extend(list(col_str))
        cake.append(col)

    for row in range(rows):
        if cake[row] == ['?'] * cols:
            continue

        first_letter = 0
        for col in range(cols):
            if cake[row][col] != '?':
                first_letter = col
                break

        last_seen = cake[row][first_letter]
        for col in range(cols):
            if cake[row][col] == '?':
                cake[row][col] = last_seen
            else:
                last_seen = cake[row][col]

    first_row = []
    for row in range(rows):
        if cake[row][0] != '?':
            first_row = cake[row]
            break

    last_seen_row = first_row
    for row in range(rows):
        if cake[row][0] == '?':
            cake[row] = last_seen_row
        else:
            last_seen_row = cake[row]

    for row in range(rows):
        print(''.join(cake[row]))
    return 0

##############################
#    CODE JAM BOILERPLATE    #
##############################


def read_ints(input, n=1):
    """ Read n integers from input - all on one line, space separated """
    return (int(st) for st in read_strs(input, n))


def read_strs(input, n=1):
    """ Read n strings from input - all on one line, space separated """
    return input.pop(0).rstrip("\n").split(" ")

# GCJ boiler plate...call run_case for each case given
if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)
    lines = sys.stdin.readlines()
    sys.stdin = open('/dev/tty')
    num_cases = int(lines.pop(0))
    for case_num in range(num_cases):
        print("Case #{}:".format(case_num + 1))
        run_case(lines)
