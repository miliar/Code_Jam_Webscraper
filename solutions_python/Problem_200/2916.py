

def read_input():
    line_numbers = int(raw_input())  # read a line with a single integer
    lines = []
    for i in xrange(1, line_numbers + 1):
        lines.append(raw_input())
    return line_numbers, lines


def handle_case(case):
    snum = case[:]
    for i in xrange(len(snum) - 1):
        for j in xrange(i + 1, len(snum)):
            if int(snum[i]) < int(snum[j]):
                break
            elif int(snum[i]) > int(snum[j]):
                newd = str(int(snum[i]) - 1)
                return int(snum[:i] + newd + "9" * (len(snum) - (i + 1)))
    return int(snum)


def main():
    res = ""
    case_counter, cases = read_input()
    for i in xrange(int(case_counter)):
        case = cases[i]
        case_result = handle_case(case)
        res += "Case #{}: {}\n".format((i + 1), case_result)

    print res[:-1]

if __name__ == '__main__':
    main()
