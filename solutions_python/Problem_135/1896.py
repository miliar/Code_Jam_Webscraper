__author__ = 'Bill'

import sys, time

def parse_case(file):
    a1 = int(file.readline()) - 1
    cards1 = []
    for i in range(4):
        cards1.append( map(int, file.readline().split()) )
    a2 = int(file.readline()) - 1
    cards2 = []
    for i in range(4):
        cards2.append( map(int, file.readline().split()) )

    return a1, cards1, a2, cards2

def process_case(case):
    a1, cards1, a2, cards2 = case
    #print(cards1[a1], cards2[a2])

    result_set = set(cards1[a1]) & set(cards2[a2])
    if len(result_set) == 1:
        result = result_set.pop()
    elif len(result_set) > 1:
        result = 'Bad magician!'
    else:
        result = 'Volunteer cheated!'

    return result

if __name__ == '__main__':
    t0 = time.clock()

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.in"

    input_file = open(filename, "r")
    output_file = open(filename.replace('in','out'), "w")
    case_count = int(input_file.readline())
    for i in range(case_count):
        result = process_case(parse_case(input_file))
        output_line = 'Case #%d: %s\n' % (i+1, result)
        print(output_line)
        output_file.writelines(output_line)

    input_file.close()
    output_file.close()

    print('Total Time: %s' % str(time.clock() - t0))