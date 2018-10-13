#codeing=utf8

import sys


def main(infile, outfile):
    lines = open(infile, 'r').readlines()
    case_num = int(lines[0].strip())
    for i in range(case_num):
        case = lines[10*i + 1:10*i + 11]
        res = get_result(case, i)
        open(outfile, 'a').write('%s\n' % res)


def get_result(case, index):
    index += 1
    first = int(case[0].strip())
    first_set = set(case[first].strip().split())
    second = int(case[5].strip())
    second_set = set(case[5+second].strip().split())
    common = first_set.intersection(second_set)
    if not common:
        return 'Case #%d: Volunteer cheated!' % index
    if len(common) == 1:
        return 'Case #%d: %s' % (index, common.pop())
    if len(common) > 1:
        return 'Case #%d: Bad magician!' % index


main(sys.argv[1], sys.argv[2])