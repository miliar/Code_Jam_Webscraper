#! /usr/bin/env python
#coding=utf-8

def solve(icase, case_input):
    case_output = 'Case #%i: '%icase
    
    comb = {}
    oppo = {}
    
    raw = case_input[0].split()
    ii = 0
    C = int(raw[ii])
    ii += 1
    if C:
        for i in xrange(ii, ii+C):
            comb[raw[i][0]] = {raw[i][1]:raw[i][2]}
            comb[raw[i][1]] = {raw[i][0]:raw[i][2]}
        ii += C
    D = int(raw[ii])
    ii += 1
    if D:
        for i in xrange(ii, ii+D):
            oppo[raw[i][0]] = raw[i][1]
            oppo[raw[i][1]] = raw[i][0]
        ii += D
    N = int(raw[ii])
    ii += 1
    ss = raw[ii]
    
#    print ss
#    print comb
#    print oppo
    
    rr = []
    for c in ss:
        rr.append(c)
        if len(rr) > 1:
            if (rr[-1] in comb) and (rr[-2] in comb[rr[-1]]):
                t = comb[rr[-1]][rr[-2]]
                rr.pop()
                rr[-1] = t
            elif rr[-1] in oppo:
#                for i in xrange(len(rr) - 2, -1, -1):
                for i in xrange(len(rr) - 1):
                    if rr[i] in oppo[rr[-1]]:
#                        rr = rr[:i]
                        rr = []
                        break

    case_output += '['
    if len(rr) > 0:
        for c in rr[:-1]:
            case_output += '%c, '%c
        case_output += rr[-1]
    case_output += ']'
    
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
    test_data = """5
    0 0 2 EA
    1 QRI 0 4 RRQR
    1 QFT 1 QF 7 FAQFDFQ
    1 EEZ 1 QE 7 QEEEERA
    0 1 QW 2 QW
    """
    use_test_data = False
    
    test_file = 'B-small-attempt2.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()