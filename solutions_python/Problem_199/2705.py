
def read_input():
    line_numbers = int(raw_input())  # read a line with a single integer
    lines = []
    for i in xrange(1, line_numbers + 1):
        lines.append(raw_input())
    return line_numbers, lines


def handle_case(case):
    row = case.split(" ")[0]
    flipper = int(case.split(" ")[1])
    count = 0
    for i in xrange(len(row) - flipper + 1):
        if row[i] == "-":
            count += 1
            row = replace(row, i, flipper)
    if row.find("-") == -1:
        return count
    return "IMPOSSIBLE"


def replace(string, start, leng):
    res = ""
    for l in string[start : start + leng]:
        if l == "+":
            res += "-"
        else:
            res += "+"
    return string[:start] + res + string[start + leng:]


def main():
    res = ""
    case_counter, cases = read_input()
    for i in xrange(int(case_counter)):
        case = cases[i]
        case_result = handle_case(case)
        res += "Case #{}: {}\n".format((i + 1), case_result)

    print res[:-1],

if __name__ == '__main__':
    main()
