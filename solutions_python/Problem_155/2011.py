__author__ = 'rsnair2'

from sys import argv


def count_num_persons_needed(shyness):
    num_standing = 0
    need_to_invite = 0
    for i in range(0, len(shyness)):
        if num_standing >= i:
            num_standing += shyness[i]
        else:
            need_to_invite += i - num_standing
            num_standing += shyness[i] + (i - num_standing)

    return need_to_invite


def parse_input(filename):
    fp = open(filename)
    num_test_cases = int(fp.readline())

    tests = list()
    for i in range(0, num_test_cases):
        raw = fp.readline()
        max_shyness = int(raw.split()[0])
        shyness = []

        for j in range(0, max_shyness + 1):
            shyness.append(int(raw.split()[1][j]))

        tests.append(shyness)
    fp.close()

    return tests


def main(infile, outfile):
    parsed = parse_input(infile)

    fp = open(outfile, 'w')
    for i in range(0, len(parsed)):
        s = 'Case #' + str(i + 1) + ': ' + \
            str(count_num_persons_needed(parsed[i])) + '\n'
        fp.write(s)
    fp.close()


if __name__ == '__main__':
    main(argv[1], argv[2])