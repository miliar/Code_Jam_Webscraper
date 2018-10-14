#!/usr/bin/python

import sys

def get_tidy(inp):
    inp = list(map(int, list(str(inp))))
    i = 0
    while i < len(inp)-1:
        if inp[i] > inp[i+1]:
            #print('i = {:}'.format(i))
            #print('{:} > {:}'.format(inp[i], inp[i+1]))
            inp[i] -= 1
            for j in range(i+1, len(inp)):
                inp[j] = 9
            if i != 0:
                i-=1

            #print(inp)
        else:
            i+=1
    return int(''.join(map(str, inp)))



with open(sys.argv[1], 'r') as f:
    cases = int(f.readline())
    for case in range(cases):
        N = int(f.readline())
        print("Case #{:}: {:}".format(case+1, get_tidy(N)))


