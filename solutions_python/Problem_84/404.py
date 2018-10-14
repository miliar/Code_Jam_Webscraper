#! /usr/bin/env python
#coding=utf-8

def solve(icase, case_input):
#    for _d in case_input:
#        print _d
    case_output = 'Case #%i: '%icase
    R, C = [int(x) for x in case_input[0].split()]
    mm = []
    for x in case_input[1:]:
        mm.append(list(x))
    bimp = False
    for i in xrange(R):
        for j in xrange(C):
            if mm[i][j] == '#':
                if i+1 >= R or j+1 >= C:
                    bimp = True
                    break
                elif mm[i][j+1] == '#' and mm[i+1][j] == '#' and mm[i+1][j+1] == '#':
                    mm[i][j] = '/'
                    mm[i+1][j+1] = '/'
                    mm[i][j+1] = '\\'
                    mm[i+1][j] = '\\'
                else:
                    bimp = True
                    break
        if bimp:
            break
    if bimp:
        case_output += '\nImpossible'
    else:
        for s in mm:
            case_output += '\n%s'%''.join(s)
    
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
        caseLineNum = int(data[iLine].split()[0]) + 1
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
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##..
    """
    use_test_data = False    
    
    test_file = 'A-large.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()