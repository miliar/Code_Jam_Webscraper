# Python3 script

import sys


def compileCase(case):
    result = []
    i = 0
    
    while i < len(case):
        if case[i] != '(':
            result.append(case[i])
        else:
            sub_result = []
            i += 1
    
            while case[i] != ')':
                sub_result.append(case[i])
                i += 1
            
            result.append(sub_result)
        
        i += 1  
    
    return result


def main():

    filename = "A-large.in"
    output = open('output', 'w')

    with open(filename) as f:

        L, D, N = [int(x) for x in f.readline().split()]

        word_list = []
        for i in range(D):
            word_list.append(f.readline().rstrip())
    
        case_no = 0
        
        for case in f:
            case_no += 1
            matches = 0
            
            compiled_case = compileCase(case.rstrip())
            
            for word in word_list:
                for word_char, case_char in zip(word, compiled_case):
                    if word_char not in case_char:
                        break
                else:
                    matches += 1
                
            output.write("Case #{}: {}\n".format(case_no, matches))
    
    output.close()


main()