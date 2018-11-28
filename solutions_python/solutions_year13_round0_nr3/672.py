# pre-computed fair and square numbers
FAIR_AND_SQUARE = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001,
                   102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201,
                   12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201,
                   1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321,
                   1234567654321, 4000008000004, 4004009004004]


def solve(config):
    low = config[0]
    high = config[1]
    count = 0

    for fsn in FAIR_AND_SQUARE:
        if fsn >= low and fsn <= high:
            count += 1
    return count


def main():
    f = open("in.txt")
    lines = f.readlines()

    num_tests = int(lines[0].strip())

    configs = []

    line_no = 1
    for i in range(num_tests):
        line = lines[line_no].strip().split(" ")
        line_no += 1
        configs.append([int(x) for x in line])

    case_num = 1
    for config in configs:
        ret = solve(config)
        if ret:
            print "Case #" + str(case_num) + ": " + str(ret)
        else:
            print "Case #" + str(case_num) + ": " + str(ret)
        case_num += 1


if __name__ == '__main__':
    main()
