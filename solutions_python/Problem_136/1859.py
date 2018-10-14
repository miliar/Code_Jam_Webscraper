__author__ = 'Bill'

import sys, time

def parse_case(file):
    return map(float, file.readline().split())

def process_case(case):
    c, f, x = case
    p = 2.0
    roi = c/f
    result = 0

    if c >= x:
        return x/p

    while True:
        result += c/p
        if roi < (x-c)/p:
            p += f
        else:
            result += (x-c)/p
            break

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