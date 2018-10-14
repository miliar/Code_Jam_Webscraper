#! /usr/bin/env python
#coding=utf-8


def ff(kk, nn, ii, ga):
    jj = ii
    ss = 0
    while kk >= ss + ga[jj]:
        ss += ga[jj]
        jj = (jj + 1) % nn
    return jj, ss
    
    
def solve(icase, case_input):
    case_output = 'Case #%d: '%icase
    
    R, k, N = [int(x) for x in case_input[0].split()]
    gg = [int(x) for x in case_input[1].split()]
    
    tt = sum(gg)
    if k >= tt:
        case_output += '%d'%(R * tt)
        return case_output
    
    rslt = [0] * N
    rslt_r = [0] * N
    icurrent = 0
    for i in range(1, R + 1):
        inext, s = ff(k, N, icurrent, gg)
        rslt[icurrent] = s
        rslt_r[icurrent] = i
        if rslt[inext] != 0:
            break
        icurrent = inext
    else:
        case_output += '%d'%sum(rslt)
        return case_output
    
    r_pre = rslt_r[inext] - 1
    r_cyc = i - r_pre
    rrr = [0] * (r_cyc + 1)
    for i in range(N):
        if rslt_r[i] > r_pre:
            rrr[rslt_r[i] - r_pre] = rslt[i]
    
    for i in range(1, r_cyc + 1):
        rrr[i] += rrr[i - 1]
    
    result = sum(rslt)
    nn, rr = divmod(R - r_cyc - r_pre, r_cyc)
    result += nn * rrr[-1] + rrr[rr]
    
    case_output += '%d'%result
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
    test_data = """3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3"""
    use_test_data = False
    
    test_file = 'C-small-attempt2.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()
    