'''
Created on 3 Sep 2009

@author: Oliver
'''
import re
import string

if __name__ == '__main__':
    filepath = raw_input('-->')
    inputfile = open(filepath, 'r')
    outputfile = open(filepath + 'output', 'w')
    output = []
    language = []
    rules = []
    for line in inputfile:
        vars = line.strip('\n').split(' ')
        if len(vars) > 1:
            L = int(vars[0])
            D = int(vars[1])
            N = int(vars[2])
            continue
        if D > 0:
            D -= 1
            language.append(vars[0])
        elif N > 0:
            N -= 1
            output.append(0)
            rules.append(vars[0].replace('(','[').replace(')',']'))
            
    for i in range(len(rules)):
        for case in language:
            if re.match(rules[i], case):
                output[i] += 1
    
    count = 0
    for out in output:
        count += 1
        outputfile.write("Case #" + str(count) + ": " + str(out) + "\n")
    