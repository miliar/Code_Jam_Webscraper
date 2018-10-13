import re

def parse(name):
    in_file = open('%s.in' % name, 'r')
    cases = int(in_file.readline())
    lines = []
    for case in range(cases):
        strings = []
        string_count = int(in_file.readline())
        for i in range(0, string_count):
            strings.append(in_file.readline().strip())
        solution = solve(strings)
        line = 'Case #%s: %s\n' % (case + 1, solution)
        print line
        lines.append(line)
    in_file.close()
    out_file = open('%s.out' % name, 'w')
    out_file.writelines(lines)
    out_file.close()

def solve(strings):
    group_matrix = []
    lengths = []
    reference = None
    result = 'Fegla Won'
    for string in strings:
        groups = re.findall(r'((.)\2*)', string)
        base = ''.join([i[1] for i in groups])
        if reference:
            if base != reference:
                break
        else:
            reference = base
        group_matrix.append([i[0] for i in groups])
    else:
        deviation = 0
        rotated_matrix = zip(*group_matrix[::-1])
        for group in rotated_matrix:
            group = list(group)
            valid = 0
            total = len(group)
            while True:
                valid = 0
                for i, string in enumerate(group):
                    if len(string) > 0:
                        valid += 1
                    group[i] = string[1:]
                if valid:
                    if valid != total:
                        deviation += 1
                else:
                    break
        result = deviation
    return result

parse('A-small-attempt0')
