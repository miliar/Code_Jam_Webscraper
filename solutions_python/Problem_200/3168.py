import os
import sys
import itertools


def output_format(string_number,test_case):
    output = "Case #%d:" % (test_case+1)
    output += " %s" % str(string_number)
    output +="\n"
    return output

def to_digits(s):
    return [int(d) for d in str(s)][::-1]

def to_str(l):
    s = ""
    for d in l:
        s+= str(d)
    return s


if __name__ == "__main__":
    # f = open("A-small-practice.in",'r')
    f = open("/home/mike/Desktop/codejam/B-large.in", 'r')
    test_cases = int(f.readline())
    out = open("/home/mike/Desktop/codejam/results_B_large.txt", 'w')

    print test_cases
    for case in range(test_cases):
        inp = f.readline().strip("\n")
        rev = to_digits(inp)
        result = ""
        highest = inp[-1]
        print highest
        rev = inp[::-1]
        if len(inp) == 1:
            result = inp
        else:
            for i, char in enumerate(rev):
                if char > highest:
                    if int(char) - 1 == 0:
                        digit = '0'
                    else:
                        digit = str(int(char)-1)
                    result = '9'*i + digit + rev[i+1:]
                    #print 'progress', result
                    highest = digit
                else:
                    highest = char

            result = result[::-1]
            if result == '':
                result = inp
            print result, case
            #result = result if result[0] not '0' else result[1:]
            if result[0] == '0':
                result = result[1:]

        output = output_format(result, case)
        out.write(output)


