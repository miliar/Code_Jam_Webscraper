#! /usr/bin/env python
#coding=utf-8

fn = lambda x, y: (x|y) - (x&y)

def solve(icase, case_input):
    case_output = 'Case #%i: '%icase
    
    data = [int(x) for x in case_input[1].split()]
    
    if 0 == reduce(fn, data):
        case_output += '%d'%(sum(data) - min(data))
    else:
        case_output += 'NO'
    
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
    caseLineNum = 2
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
    test_data = """2
    5
    1 2 3 4 5
    3
    3 5 6
    """
    use_test_data = False
    
    test_file = 'C-large.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()