"""
Created on Apr 17, 2015

@author: umnik700@gmail.com
"""

# INPUT_FILE = 'test-input.txt'
# OUTPUT_FILE = 'test-output.txt'

# INPUT_FILE = 'A-small-attempt0.in'
# OUTPUT_FILE = 'A-small-attempt0.out'

INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large.out'

total_tests = None
tests = []


def process_test(intervals, mashrooms):

    y = 0
    z = 0
    
    i_prev =  mashrooms[0]
    rate = 0
    for i in mashrooms[1:]:
        if(i < i_prev):
            new_rate = i_prev - i
            y += new_rate

            if(new_rate > rate):
                rate = new_rate

        i_prev = i

    for i in mashrooms[0:-1]:
        eat = min(rate, i)
        z += eat


    print 'process_test', (intervals, mashrooms)
    return y, z

with open(INPUT_FILE) as f:

    input_data = list(f)
    index = 0
    while index < len(input_data):

        print 'index', index

        line = input_data[index].strip()
        if(not line):
            index += 1
            continue

        if(total_tests is None):
            total_tests = int(line)
            print 'total_tests', total_tests
            index += 1
            continue

        intervals = int(line)
        index += 1
        mashrooms = [int(i) for i in input_data[index].strip().split(' ')]

        if(intervals != len(mashrooms)):
            print 'intervals', intervals, 'mashrooms', len(mashrooms), mashrooms
            raise Exception('invalid test')

        tests += [(intervals, mashrooms)]
        index += 1

if(total_tests != len(tests)):
    print 'tests', len(tests)
    raise Exception('invalid number of tests')

print '-' * 70
print 'input data'
print '-' * 70
for test in tests:
    print test
print '-' * 70

case_number = 0

with open(OUTPUT_FILE, 'wb') as o:
    for s_max, shyness in tests:
        case_number += 1

        y, z = process_test(s_max, shyness)

        print "Case #%d: %d %d" % (case_number, y, z)
        o.write("Case #%d: %d %d\n" % (case_number, y, z))
