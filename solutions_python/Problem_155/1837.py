"""
Created on Apr 11, 2015

@author: umnik700@gmail.com
"""

# INPUT_FILE = 'test-input.txt'
# OUTPUT_FILE = 'test-output.txt'

# INPUT_FILE = 'A-small-attempt0.in'
# OUTPUT_FILE = 'A-small-attempt0.out'

INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large.out'

def process_test(s_max, shyness):
    cumulative_list = []
    for s in shyness:
        cumulative_list += [s + (cumulative_list[-1] if cumulative_list else 0)]
    
    ideal_list = [i for i in xrange(1, s_max + 2)]
    
    result = 0

    for i in xrange(len(cumulative_list)):
        if(ideal_list[i] > cumulative_list[i]):
            value = ideal_list[i] - cumulative_list[i]
            if(value > result):
                result = value
    print shyness, cumulative_list, ideal_list
    return result

total_tests = None
tests = []

with open(INPUT_FILE, 'rU') as f:

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

        s_max, shyness_string = line.strip().split(' ')
        s_max = int(s_max)
        shyness = [int(i) for i in shyness_string]

        if(s_max + 1 != len(shyness)):
            print 's_max+1', s_max + 1, 'shyness', len(shyness), shyness
            raise Exception('invalid test')

        tests += [(s_max, shyness)]
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

        result = process_test(s_max, shyness)

        print "Case #%d: %d" % (case_number, result)
        o.write("Case #%d: %d\n" % (case_number, result))
    


