def get_input(filename):
    result = []
    f = open(filename)
    lines = f.readlines()
    cases = int(lines[0])
    for i in range(1, cases + 1):
        case = lines[i].replace("\n", "").split()
        case_result = []
        for j in range(int(case[0]) + 1):
            case_result.append(int(case[1][j]))
        result.append(case_result)
    f.close()
    return cases, result


def set_output(filename, data):
    f = open(filename, 'w')
    for case in data:
        f.write('Case #' + str(case[0]) + ': ' + str(case[1]))
        if case[0] < len(data):
            f.write('\n')
    f.close()


def count(filename):
    cases, data = get_input(filename)
    results = []
    for i in range(cases):
        total_up = 0
        friends = 0
        for required in range(len(data[i])):
            while total_up < required:
                friends += 1
                total_up += 1
            total_up += data[i][required]
        results.append([i + 1, friends])
    set_output(filename + '.out', results)
    print(results)


count('A-large.in')