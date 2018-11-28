def solve(config):
    valids = [[False for i in range(len(config[0]))] for j in range(len(config))]
    for row in range(len(config)):
        for col in range(len(config[0])):
            cell = config[row][col]
            valids[row][col] = cell >= max(config[row])

    # rotate the matrix
    config_rotate = zip(*config[::-1])
    valids_rotate = zip(*valids[::-1])

    config = []
    valids = []

    for row in config_rotate:
        config.append(list(row))

    for row in valids_rotate:
        valids.append(list(row))

    for row in range(len(config)):
        for col in range(len(config[0])):
            cell = config[row][col]
            valids[row][col] = cell >= max(config[row]) or valids[row][col]

    for row in valids:
        if False in row:
            return False

    return True


def main():
    f = open("in.txt")
    lines = f.readlines()

    num_tests = int(lines[0].strip())

    configs = []

    line_no = 1
    for i in range(num_tests):
        size = lines[line_no].strip().split(" ")
        line_no += 1
        rows = int(size[0])
        configs.append([])
        for j in range(rows):
            configs[i].append([int(height) for height in lines[line_no].strip().split()])
            line_no += 1

    case_num = 1

    for config in configs:
        ret = solve(config)
        if ret:
            print "Case #" + str(case_num) + ": YES"
        else:
            print "Case #" + str(case_num) + ": NO"
        case_num += 1


if __name__ == '__main__':
    main()
