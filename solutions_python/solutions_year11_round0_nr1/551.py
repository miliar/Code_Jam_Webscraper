#! /usr/bin/env python
#coding=utf-8

def solve(icase, case_input):
    case_output = 'Case #%i: '%icase
    
    raw = case_input[0].split()
    N = int(raw[0])
    turn = raw[1::2]
    orange = []
    blue = []
    for i, v in enumerate(turn):
        if v == 'O':
            orange.append(int(raw[2*i+2]))
        else:
            blue.append(int(raw[2*i+2]))
    for i in xrange(len(orange) - 1, 0, -1):
        orange[i] = abs(orange[i] - orange[i - 1]) + 1
    for i in xrange(len(blue) - 1, 0, -1):
        blue[i] = abs(blue[i] - blue[i-1]) + 1
#    print turn
#    print orange
#    print blue
    
    step = 0
    for t in turn:
        if t == 'O':
            a = orange
            b = blue
        else:
            a = blue
            b = orange
        s = a.pop(0)
        step += s
        if len(b):
            s = b[0] - s
            if s < 1:
                s = 1
            b[0] = s
            
    

    case_output += '%d'%step
    
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
    4 O 2 B 1 B 2 O 4
    3 O 5 O 8 B 100
    2 B 2 B 1
    """
    use_test_data = False
    
    test_file = 'A-large.in'
    if not use_test_data and '' != test_file:
        input_file = open(test_file)
        output_file = open(test_file + '.out', 'w')
    
    main()