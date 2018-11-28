import math

def fair_and_square(start, end):
    count = 0
    for i in xrange(start, end + 1):
        if str(i) == str(i)[::-1]:
            if int(math.sqrt(i)) == math.sqrt(i) and str(int(math.sqrt(i))) == str(int(math.sqrt(i)))[::-1]:
                count += 1
    return count

def read_input(filename):
    handle = open(filename, 'r')
    count = int(handle.readline())
    test_cases = []
    for i in xrange(count):
        test_cases.append(handle.readline().split())
    return test_cases

test_cases = read_input('C-small-attempt0.in')
for i in xrange(len(test_cases)):
    case = test_cases[i]
    print 'Case #' + str(i + 1) + ': ' + str(fair_and_square(int(case[0]), int(case[1])))
    