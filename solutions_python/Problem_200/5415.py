import sys
def is_non_descending(number):
    digits = []
    if number < 10:
        return True

    while (number != 0):
        digits.append(number % 10)
        number /= 10

    digits.reverse()
    # print digits
    for i in xrange(len(digits)):
        for j in xrange(i, len(digits)):
            # print "COMPARING %d AND %d" % (digits[i], digits[j])
            if digits[i] > digits[j]:
                # print "FALSE"
                return False
    return True
    # return all(digits[i] <= digits[i+1] for i in xrange(len(digits)-1))



if __name__ == '__main__':
    test_cases = 0
    case_data = []
    with open(sys.argv[1], 'r') as f:
        test_cases = int(f.readline())
        for i in range(test_cases):
            case = int(f.readline())
            case_data.append(case)

    case_num = 1
    answers = []
    for case in case_data:
        print case
        while not is_non_descending(case):
            case -= 1
            # print case
        answers.append((case_num, case))
        case_num += 1

    with open('solution.out', 'w') as f:
        for ans in answers:
            f.write('Case #%d: %d\n' % (ans[0], ans[1]))
