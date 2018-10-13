#! /usr/bin/env python
#coding=utf-8

def eu(x, y):
    xx = min(x, y)
    yy = max(x, y)
    while True:
        d, r = divmod(yy, xx)
        if 0 == r:
            return xx
        xx, yy = r, xx
        

def solve(icase, case_input):
    case_output = 'Case #%i: '%icase
    
    raw = case_input[0].split()
    N = int(raw[0])
    pd = int(raw[1])
    pg = int(raw[2])
    
    if pg == 100:
        if pd != 100:
            case_output += 'Broken'
        else:
            case_output += 'Possible'
    elif pg == 0:
        if pd != 0:
            case_output += 'Broken'
        else:
            case_output += 'Possible'
    elif pd == 0:
        case_output += 'Possible'
    else:
        bd = 100 / eu(100, pd)
        if bd <= N:
            case_output += 'Possible'
        else:
            case_output += 'Broken'
    

#    case_output += '%d'%step
    
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
    test_data = """3
1 100 50
10 10 100
9 80 56
    """
    use_test_data = False
    
    test_file = 'A-large.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()