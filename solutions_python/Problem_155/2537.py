#!/usr/bin/env python
"""
Author: Joyce
Date:2015.4.11
"""

from sys import argv

def read_file(lines):
    result = []
    case = int(lines[0])
    for line in lines[1:]:
        max_shy = int(line.strip().split()[0])
        result.append([max_shy]+map(int,list(line.strip().split()[1])))
    return result

def invite(result,output):
    outfile = open(output,'w')
    for idx,case in enumerate(result):
        outfile.write('Case #%d: ' % (idx+1)) 
        max_shy = case[0]
        del case[0]
        num_au,num_inv = 0,0
        for idx,num in enumerate(case):
            if num and num_au-idx < 0:
                inv = idx-num_au
                num_au += inv
                num_inv += inv
            num_au += num
        outfile.write('%d\n' % num_inv)
    outfile.close()

if __name__ == '__main__':
    infile = open(argv[1]).readlines()
    result = read_file(infile)
    output = argv[2]
    invite(result,output)

                    

