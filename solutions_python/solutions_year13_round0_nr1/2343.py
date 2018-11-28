#!/usr/bin/python

import sys
import re

def solve(input):
    def extract(input):
        extracted=[]
        extracted.append(input[0]+input[1]+input[2]+input[3])
        extracted.append(input[4]+input[5]+input[6]+input[7])
        extracted.append(input[8]+input[9]+input[10]+input[11])
        extracted.append(input[12]+input[13]+input[14]+input[15])
        extracted.append(input[0]+input[4]+input[8]+input[12])
        extracted.append(input[1]+input[5]+input[9]+input[13])
        extracted.append(input[2]+input[6]+input[10]+input[14])
        extracted.append(input[3]+input[7]+input[11]+input[15])
        extracted.append(input[0]+input[5]+input[10]+input[15])
        extracted.append(input[3]+input[6]+input[9]+input[12])  
        return extracted

    lines=extract(input)
    for line in lines:
        if re.match( '[XT]{4}', line ): return 'X won'
        if re.match( '[OT]{4}', line ): return 'O won'
    if '.' in input: return 'Game has not completed'
    else: return 'Draw'

if __name__ == '__main__':
    with open(sys.argv[2], 'w') as out:
        with open(sys.argv[1]) as f:
            T = int(f.readline())
            for i in range(T):
                input=[]
                for _ in range(4):
                    input.extend(f.readline().strip())
                result=solve(input)
                f.readline()
                print('Case #{}: {}'.format(i+1,result), file=out)
