'''
Created on May 11, 2014

@author: sergey

Problem A. Part Elf
'''

import os


def get_data(fullpath):
    if(not os.path.exists(fullpath)):
        print 'file does not exist'
        return []

    result = []
    is_first_line = True
    line_in_test = 0
    number_of_test_cases = 0
    with open(fullpath, 'r') as input_file:
        for line in input_file:

            print '---', line_in_test, line
            if(is_first_line):
                is_first_line = False
                number_of_test_cases = int(line)
                if(number_of_test_cases >= 1 and number_of_test_cases <= 100):
                    line_in_test = 1
                    continue

                print 'invalid number of test cases', number_of_test_cases
                return []

            else:
                p, q = [int(i) for i in line.strip().split('/')]
                if(not (p >= 1 and p < q and q <= 1000000000000)):
                    print "invalid p or q", p, q
                    return []
                result += [{
                            'p': p,
                            'q': q
                             }]


    print 'expected', number_of_test_cases, 'test cases, got', len(result)
    if(number_of_test_cases != len(result)):
        return []

    return result

def get_result(p, q):
    result = 0
    extra_div = 0
    n_power = 0

    for i in xrange(1, 41):
        n_power = (2 ** i)
        if(q < n_power):
            extra_div = q / (2 ** (i - 1))
            break
        elif(q == n_power):
            result += 1
            break

        if(q % n_power == 0):
            result += 1
        else:
            extra_div = q / (2 ** (i - 1))
            break

    if(p != 1 and (q % p) != 0):
        j_power = 0
        p_remainder = p % n_power
        for j in xrange(1, 41):
            j_power = (2 ** j)
            if(p_remainder < j_power):
                break
            result = result - 1

    if(extra_div != 0):
        if(p % extra_div == 0):
            return str(result)
        else:
            return "impossible"

    if(result > 40):
        return "impossible"

    return str(result)

def main():

    input_filename = 'A-small-attempt0.in'
    output_filename = 'A-small-attempt0.out'

    data = get_data(input_filename)
    for item in data:
        print item

    print '-' * 75

    with open(output_filename, 'wb') as output_file:
        case_number = 0
        for item in data:
            case_number += 1

            if(case_number == 2):
                pass

            result = get_result(item['p'], item['q'])

            print 'Case #%d: %s' % (case_number, result)
            output_file.write('Case #%d: %s\n' % (case_number, result))

if __name__ == "__main__":
    main()
