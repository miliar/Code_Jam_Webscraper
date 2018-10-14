#! /usr/bin/env python
#coding=utf-8

    
def solve(icase, case_input):
    case_output = 'Case #%i: '%icase
    
    N, K = [int(x) for x in case_input[0].split()]
    
    nn = 2 ** N
    kk = K + 1
    if 0 == kk % nn:
        case_output += 'ON'
    else:
        case_output += 'OFF'
    
    return case_output


def main():
    global use_test_data
    global test_data
    global input_file
    global output_file
    
    if use_test_data:
        data = [x.strip() for x in test_data.split('\n')]
    else:
        data = [x.strip() for x in input_file.readlines()]
    
    T = int(data[0])
    iLine = 1
    caseLineNum = 1
    for icase in range(1, T + 1):
        input = []
        for i in range(caseLineNum):
            input.append(data[iLine])
            iLine += 1
        rslt = solve(icase, input)
        print rslt
        if not use_test_data:
            print >> output_file, rslt
    
    if not use_test_data:
        input_file.close()
        output_file.close()
    
    
if __name__ == '__main__':
    test_data = """4
    1 0
    1 1
    4 0
    4 47
    """
    use_test_data = False
    
    test_file = 'A-large.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()