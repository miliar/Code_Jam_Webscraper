'''
Created on 14/04/2012

@author: Rachum
'''

def regular_result(score):
    div = score / 3
    mod = score % 3
    if mod == 0:
        return (div, div, div)
    elif mod == 1:
        return (div+1, div, div)
    else:
        return (div+1, div+1, div)
    
def surprising_result(score):
    div = score / 3
    mod = score % 3
    if mod == 0:
        return (div+1, div, div-1)
    elif mod == 1:
        return (div+1, div+1, div-1)
    else:
        return (div+2, div, div)
    
def solve_case(s, p, scores):
    result = 0
    for score in scores:
        if max(regular_result(score)) >= p:
            result += 1
        elif s > 0 and score > 0:
            if max(surprising_result(score)) >= p:
                result += 1
                s -= 1
    return result





with open('input.in', 'rt') as inputfile, open('output.txt', 'wt') as outputfile:
    num_of_testcases = int(inputfile.readline())
    for i, line in enumerate(inputfile.readlines()):
        n, s, p = (int(item) for item in line.split()[:3])
        scores = tuple(int(item) for item in line.split()[3:])
        print("Case #%d: %s" % (i+1, solve_case(s, p, scores)), file=outputfile)
        
        
