#!/usr/bin/env python

def step(lresult,lp,input,lpot):
    pot = max(abs(lp-input)-lpot,0) + 1
    result = lresult +  pot
    return result,input, pot


if __name__ == '__main__':
    f = open('input')
    a = int( f.readline() )
    for i in range(a):
        bp = 1
        op = 1
        result = 0
        bpot = 0
        opot = 0
        line = f.readline().split()
        n = int(line[0])
        k = 1
        for j in range(n):
            if line[k] == 'B':
                result, bp ,time = step(result,bp,int(line[k+1]),bpot) 
                opot += time
                bpot = 0
            if line[k] == 'O':
                result, op ,time = step(result,op,int(line[k+1]),opot) 
                bpot += time
                opot = 0
            k = k + 2
        print "Case #"+str(i+1)+":", result
