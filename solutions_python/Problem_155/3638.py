def solve(case):
    #return 'PLACE HOLDER'
    case_len = int(case[0])
    case_list = []
    counter = 0

    for x in xrange(2,case_len+3):
    	case_list.append(int(case[x]))

    needed = case_len
    standing = case_list[0]

    for x in xrange(len(case_list)-1):
        if case_list[x+1] > 0:
            if standing >= x+1:
                standing += case_list[x+1]
            else:
                add = (x+1) - standing
                standing += case_list[x+1] + add
                counter += add

    return counter

if __name__ == '__main__':
    inputCases = input()

    for testCase in xrange(1, inputCases+1):
        case = raw_input()
        print 'Case #%i: %s' % (testCase,str(solve(case)))
