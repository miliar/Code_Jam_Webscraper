"""
Created on Apr 11, 2015

@author: umnik700@gmail.com
"""

# INPUT_FILE = 'test-input.txt'
# OUTPUT_FILE = 'test-output.txt'

INPUT_FILE = 'D-small-attempt1.in'
OUTPUT_FILE = 'D-small-attempt1.out'

def process_test(x, r, c):

    if((r * c) < x):
        return 'RICHARD'

    if((r * c) % x != 0):
        return 'RICHARD'

    if(r < x and c < x):
        return 'RICHARD'

    # L shapes
    if(x == 3):
        # 2 x 2
        if(min([r, c]) < 2):
            return 'RICHARD'
    if(x==4):
        # 2 x 3
        if(min([r, c]) < 2):
            return 'RICHARD'
    elif(x==5):
        # 2 x 4, 3 x 3
        if(min([r, c]) < 3):
            return 'RICHARD'
    elif(x == 6):
        # 2 x 5, 3 x 4
        if(min([r, c]) < 3):
            return 'RICHARD'

#     # diagonal
    if(x==4):
        if(min([r, c])< 3):
            return 'RICHARD'
    elif(x==5):
        if(min([r, c])< 4):
            return 'RICHARD'
    elif(x == 6):
        if(min([r, c]) < 4):
            return 'RICHARD'

    # hole in the middle
    if(x >= 7):
        return 'RICHARD'

    return 'GABRIEL'

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

        x, r, c = [int(i) for i in line.strip().split(' ')]

        tests += [(x, r, c)]
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
    for x, r, c in tests:
        case_number += 1

        result = process_test(x, r, c)

        print "Case #%d: %s" % (case_number, result), x, r, c
        o.write("Case #%d: %s\n" % (case_number, result))
    


