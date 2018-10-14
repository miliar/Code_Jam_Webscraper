'''
Created on Apr 14, 2012

@author: silent
'''

import sys

def get_input(input_file):
    infile = open(input_file)
    return infile

def get_output(output_file):
    outfile = open(output_file, "w")
    return outfile

def solve(a, b, p):
    '''
    a: number of characters that I have already typed
    b: total number of characters in my password
    p: array with probability that I correctly typed
    '''
    
    r = b - a + 1
    
    if p.count(1) == a:
        return r

    pb = []
    for i in range(pow(2, a)):
        temp_p = 1
        for j in range(a):
            t = i >> (a - j - 1)
            if t & 1 == 1:
                temp_p = temp_p * ((t & 1) - p[j])
            else:
                temp_p = temp_p * p[j]
            if temp_p == 0:
                break
        pb.append(temp_p)
    
    # keep typing
    case1 = r
    case2 = r + b + 1
    expected = (pb[0] * case1) + sum(case2 * pb[1:])
    
    # enter right away
    case1 = b + 2 # 1 + b + 1
    expect = sum(case1 * pb)
    if expect < expected:
        expected = expect
    
    # press backspace i times
    for i in range(1, a + 1):
        case1 = i + r + 1 # i + b - a + 1 + 1
        case2 = i + r + b + 2
        expect = sum(case1 * pb[:i + 1]) + sum(case2 * pb[i + 1:])
        if expect < expected:
            expected = expect

    return expected

if __name__ == '__main__':
    if len(sys.argv) == 1:
        input_file = 'input.in'
    else:
        input_file = sys.argv[1]
    filename = input_file.split(".")[0]
    infile = get_input(input_file)
    outfile = get_output(filename + ".out")
    
    t = int(infile.readline())
    
    for case_num in range(t):
        [a, b] = map(int, infile.readline().split())
        p = map(float, infile.readline().split())
        result = solve(a, b, p)
        
        outfile.write("Case #%d: %.6f\n" % (case_num + 1, result))
        print "Case #%d: %.6f" % (case_num + 1, result)
    
    infile.close()
    outfile.close()
