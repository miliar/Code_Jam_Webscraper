#! /usr/bin/env python
#coding=utf-8

def eu(a, b):
    m = max(a, b)
    n = min(a, b)
    if 1 == n:
        return 1
    
    while 0 != n:
        m, n = n, m % n
        
    return m
    
def solve(icase, case_input):
    case_output = 'Case #%d: '%icase
    
    tt = [int(x) for x in case_input[0].split()]
    nn = tt[0]
    tt = tt[1:]
    tt.sort()
    gap = [tt[x] - tt[x-1] for x in range(1, len(tt))]
    mm = reduce(eu, gap)
    r = tt[0] % mm
    rslt = (0 != r) and (mm - r) or 0
    
    case_output += '%d'%rslt
    
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
3 26000000 11000000 6000000
3 1 10 11
2 800000000000000000001 900000000000000000001"""
    use_test_data = False
    
    test_file = 'B-large.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()
    