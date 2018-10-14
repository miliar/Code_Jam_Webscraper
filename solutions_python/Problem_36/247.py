#!/usr/bin/python

import sys

InputFile = "C-small-attempt0.in"
OutFile = "C-small-attempt0.out"

sample = "welcome to code jam"

def processInput(filename):
    """docstring for processInput"""
    f = open(filename)
    data = [line.strip() for line in f.readlines()]
    return data[1:]
 

def processOutput(filename, content):
    """docstring for processOutput"""
    f = open(filename, 'w')
    for i in range(len(content)):
        pass
        f.write('Case #%d: %04d\n' %(i + 1, content[i]))
    f.close()

def solve(stringLists):
    """docstring for solve"""
    ret = []
    print stringLists
    for s in stringLists:
        cnt = count(s, 0, 0)
        print cnt
        ret.append(cnt % 10000)
    return ret

def count(inputStr, beginPos, offset):
    """docstring for count"""
    ret = 0
    if offset + 1 >= len(sample):
        return inputStr.count(sample[-1], beginPos)
    else:
        begin = inputStr.find(sample[offset], beginPos)
        #print "%d %s %d %d" %(begin, sample[offset], offset, beginPos)
        if begin >= 0:
            while begin >= 0:
                ret += count(inputStr, begin + 1, offset + 1)
                begin = inputStr.find(sample[offset], begin + 1)
        else:
            return 0
    return ret
            

def main():
    """docstring for main"""
    stringLists = processInput(InputFile)
    result = solve(stringLists)
    processOutput(OutFile, result)

if __name__ == '__main__':
    main()
