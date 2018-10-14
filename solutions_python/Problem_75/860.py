#!/usr/bin/env python
# google code jam 2011
# round 1, problem B
# Joseph Lee <GengarKhan@gmail.com>
# 5/6/11

import sys

def main():
    infile = open(sys.argv[1], 'r').read().strip().split('\n')[1:]  # input
    if len(sys.argv) >= 3:  # if output file specified
        outfile = open(sys.argv[2], 'w')    # output file, 2nd cmd-line arg
    else:       # if output file unspecified, write to stdout
        outfile = sys.stdout
    casenum=1
    for i in infile:
        outfile.write('Case #%d: %s\n' %(casenum, test_case(i)))
        casenum=casenum+1
    outfile.close()
    return 0

# run test cat, return properly formatted string of list
def test_case(case_line):
    combo_ls, opp_ls, invoke_ls = parse_case(case_line)
    elem_ls = []    # resulting element list
    while len(invoke_ls) > 0:
        if len(elem_ls) == 0:   # empty element list, pop
            elem_ls.append(invoke_ls.pop(0))
        else:
            check_opp = True
            for c in combo_ls:  # check for combos
                if c[0] in elem_ls[-1] and c[1] in invoke_ls[0] or\
                    c[1] in elem_ls[-1] and c[0] in invoke_ls[0]:
                    check_opp = False   # no need to check for opposed
                    invoke_ls.pop(0)
                    elem_ls[-1] = c[2]  # change end to combo
                    break
            if check_opp == True:
                for o in opp_ls:    # check for opposed pairs
                    if o[0] in invoke_ls[0] and o[1] in elem_ls or\
                        o[1] in invoke_ls[0] and o[0] in elem_ls:
                        elem_ls = []
                        invoke_ls.pop(0)
                        check_opp = False   # opposed pair action was taken
                        break
                if check_opp == True:   # if opposing match not found
                    elem_ls.append(invoke_ls.pop(0))
    return ''.join(elem_ls.__str__().split("'"))

# parse test case line, return 3-tuple:
# list of combos, list of opposing, list of invoked chars
def parse_case(case_line):
    case_ls = case_line.strip().split(' ')
    combo_ls = []
    opp_ls = []
    invoke_ls = []
    c = int(case_ls.pop(0))     # num of combo strings
    while c > 0:
        combo_ls.append(case_ls.pop(0))
        c=c-1
    d = int(case_ls.pop(0))
    while d > 0:
        opp_ls.append(case_ls.pop(0))
        d=d-1
    case_ls.pop(0)  # int N, length of spell str, discarded
    invoke_str = case_ls.pop(0)
    for i in range(0, len(invoke_str)):  # compile list of spell chars
        invoke_ls.append(invoke_str[i])
    return combo_ls, opp_ls, invoke_ls


if __name__ == '__main__':
    main()

