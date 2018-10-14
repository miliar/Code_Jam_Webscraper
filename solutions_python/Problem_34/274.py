#!/usr/bin/python

import sys

InputFile = "A-large.in.txt"
OutFile = "A-large.out.txt"

def processInput(filename):
    """docstring for processInput"""
    f = open(filename)
    data = [line.strip() for line in f.readlines()]
    print data
    info = data[0].split(' ')
    print info
    pNum = int(info[1])
    cNum = int(info[2])
    patterns = data[1:(pNum + 1)]
    cases = []
    for i in range(pNum + 1, pNum + cNum + 1):
        tmpStr = data[i].split('(')
        print tmpStr
        c = []
        for s in tmpStr:
            if ')' in s:
                p = s.index(')')
                c.append(s[:p])
                for index in range(p + 1, len(s)):
                    c.append(s[index])
            elif s:
                for index in range(len(s)):
                    c.append(s[index])
            else:
                pass
        cases.append(c)
    print patterns
    print cases
    return patterns, cases

def processOutput(filename, content):
    """docstring for processOutput"""
    f = open(filename, 'w')
    for i in range(len(content)):
        f.write('Case #%d: %d\n' %(i + 1, content[i]))
    f.close()

def solve(patterns, cases):
    """docstring for solve"""
    ret = []
    for c in cases:
        count = 0
        for p in patterns:
            if check(p, c):
                count += 1
        ret.append(count)
    return ret

def check(pattern, case):
    """docstring for check"""
    for i in range(len(pattern)):
        if pattern[i] not in case[i]:
            return False
    return True

def main():
    """docstring for main"""
    patterns, cases = processInput(InputFile)
    result = solve(patterns, cases)
    processOutput(OutFile, result)

if __name__ == '__main__':
    main()
