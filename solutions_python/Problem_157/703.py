def ijk_multiply(inp_1, inp_2):
    inp_1_without_neg = inp_1.replace('-', '')
    inp_2_without_neg = inp_2.replace('-', '')
       
    if (inp_1_without_neg == 'i'):
        if (inp_2_without_neg == 'i'):
            output = '-'
        elif (inp_2_without_neg == 'j'):
            output = 'k'
        elif (inp_2_without_neg == 'k'):
            output = '-j'
        elif (inp_2_without_neg == ''):
            output = inp_1_without_neg
    elif (inp_1_without_neg == 'j'):
        if (inp_2_without_neg == 'i'):
            output = '-k'
        elif (inp_2_without_neg == 'j'):
            output = '-'
        elif (inp_2_without_neg == 'k'):
            output = 'i'
        elif (inp_2_without_neg == ''):
            output = inp_1_without_neg
    elif (inp_1_without_neg == 'k'):
        if (inp_2_without_neg == 'i'):
            output = 'j'
        elif (inp_2_without_neg == 'j'):
            output = '-i'
        elif (inp_2_without_neg == 'k'):
            output = '-'
        elif (inp_2_without_neg == ''):
            output = inp_1_without_neg
    else:    
        output = inp_2_without_neg
        
    if ('-' in inp_1):
        output = '-' + output
    if ('-' in inp_2):
        output = '-' + output
    output = output.replace('--', '')  
    
    return output
    
def solve(input_str):
    input_str_part = input_str.split()
    N = int(input_str_part[0])
    X = int(input_str_part[1])
    cipher = raw_input()
    O = 0 #Output is 1 for YES, 0 for NO
    if (N*X > 3):
        ijk_str = list(cipher)
        ijk_test = ''
        test = 1
        for i in range(N):
            ijk_test = ijk_multiply(ijk_test, ijk_str[i])
        if (ijk_test == ''):
            test = 0
        elif (ijk_test == '-'):
            if (X % 2 != 1):
                test = 0
        elif (ijk_test == 'i' or ijk_test == 'j' or ijk_test == 'k'):
            if (X % 4 != 2):
                test = 0
        elif (ijk_test == '-i' or ijk_test == '-j' or ijk_test == '-k'):
            if (X % 4 != 2):
                test = 0

        if (test == 1):
            ijk_bool = [0, 0, 0]
            ijk_count = ''
            not_finished = 0
            for i in range(N*X):
                ijk_count = ijk_multiply(ijk_count,ijk_str[i % N])
                if (ijk_bool[0] == 0):
                    if (ijk_count == 'i'):
                        ijk_bool[0] = 1
                        ijk_count = ''
                elif (ijk_bool[1] == 0):
                    if (ijk_count == 'j'):
                        ijk_bool[1] = 1
                        ijk_count = ''
                elif (ijk_bool[2] == 0):
                    if (ijk_count == 'k'):
                        ijk_bool[2] = 1
                        ijk_count = ''
                else:
                    not_finished = 1
                    ijk_iterator = i
                    break
            if (not_finished == 1):
                remaining_X = X - (ijk_iterator / N + 1)
                ijk_iterator = ijk_iterator % N
                
                for i in range(ijk_iterator+1, N):
                    ijk_count = ijk_multiply(ijk_count, ijk_str[i])
                
                if (ijk_test == '-'):
                    if (remaining_X % 2 == 0):
                        ijk_test = ''
                elif (ijk_test == 'i' or ijk_test == 'j' or ijk_test == 'k'):
                    if (remaining_X % 4 == 0):
                        ijk_test = ''
                    elif (remaining_X % 4 == 2):
                        ijk_test = '-'
                    elif (remaining_X % 4 == 3):
                        ijk_test = '-' + ijk_test
                elif (ijk_test == '-i' or ijk_test == '-j' or ijk_test == '-k'):
                    if (remaining_X % 4 == 0):
                        ijk_test = ''
                    elif (remaining_X % 4 == 2):
                        ijk_test = '-'
                    elif (remaining_X % 4 == 3):
                        ijk_test = ijk_test.replace('-', '')
                ijk_count = ijk_multiply(ijk_count, ijk_test)
            if (ijk_count == '' and ijk_bool == [1, 1, 1]):
                O = 1            
    elif (N == 3 and cipher == 'ijk'):
        if (X % 2 == 1):
            O = 1
    
    if (O == 0):
        output = 'NO'
    else:
        output = 'YES'
    return output

testcases = input()
    
for caseNr in xrange(1, testcases+1):
    cipher = raw_input()
    print("Case #%i: %s" % (caseNr, solve(cipher)))