# Magic Trick
# Joseph Lee

from sys import argv


def test_case(lines):
    row_num1 = int(lines[0].strip())
    row_num2 = int(lines[5].strip())
    nums1 = set(map(lambda r: int(r), lines[row_num1].strip().split(' ')))
    nums2 = set(map(lambda r: int(r), lines[row_num2 + 5].strip().split(' ')))
    answers = nums1 & nums2
    if len(answers) == 1:
        return '%d' % (list(answers)[0])
    elif len(answers) == 0:
        return 'Volunteer cheated!'
    return 'Bad magician!'


def main():
    input_fname = argv[1]
    with open(input_fname, 'r') as input_file:
        raw_lines = input_file.readlines()
    raw_lines.pop(0)    # test cases, unnecessary

    case_num = 1
    while len(raw_lines) >= 10:
        case_lines, raw_lines = raw_lines[:10], raw_lines[10:]
        print 'Case #%d: %s' %(case_num, test_case(case_lines))
        case_num += 1


if __name__ == '__main__':
    main()
