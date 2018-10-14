#! /usr/bin/env python
'''
Created on 14/04/2012

@author: laarguelless
'''

import sys

def processFile(inputFile):
    
    file = open(inputFile)
    outp = open("recicled.out","w")
    cases = file.readline()
    cases = cases[:len(cases) -1]
    cases = int(cases)
    
    for i in range(0,cases):
        line = file.readline()
        result = processInterval(line)
        result = "Case #{0}: {1}\n".format(i+1,result)
        outp.write(result)

def processInterval(line):
    pairs = 0
    line = line[:len(line) - 1]
    line = line.split(" ")
    A = int(line[0])
    B = int(line[1])
    
    
    for i in range(A,B +1):
        pairs += numberOfPairs(i,A,B)
    
    return pairs 

def numberOfPairs(number,min,max):
    s_number = str(number)
    pairs = []
    #print("number:"+ s_number)
    for i in range(-1,-len(s_number) -1,-1):        
        if(int(s_number[i]) * (10**len(s_number)/10) < max):
            
            num = s_number[i:]+s_number[:i]
            num = int(num)
            if(min <= num  <= max and num > number):
                if(not num in pairs):
                    pairs.append(num)
                
    return len(pairs)



def main():
    inputFile = False
    try:
        inputFile = sys.argv[1]
    except IndexError:
        return
    if(inputFile):
        processFile(inputFile)


if __name__ == '__main__':
    main()