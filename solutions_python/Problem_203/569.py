#!/usr/bin/env python

INFILE='/Users/linlin/Downloads/A-large.in'
#INFILE='./test.txt'

def check_r(input, r, c):
    i = int(c)
    if i == 0:
        while i < len(input[r]):
            if input[r][i] != '?':
                return input[r][i]
            i += 1
    else:
        return input[r][i-1]
    return '?'

def check_c(input, r, c):
    i = int(r)
    if i == 0:
        while i < len(input):
            if input[i][c] != '?':
                return input[i][c]
            i += 1
    else:
        return input[i-1][c]
    return '?'

def process(input):
    result = ''
    rec = {}
    r = 0 
    c = 0
    row = len(input)
    col = len(input[0])
    while r < row:
        while c < col:
            if input[r][c] == '?':
                input[r][c] = check_r(input, r,c)
            c += 1
        c = 0
        r += 1
    r = 0
    c = 0
    while r < row:
        while c < col:
            if input[r][c] == '?':
                input[r][c] = check_c(input, r,c)
            c += 1
        c = 0
        r += 1
    for r in input:
        result += ''.join(r) + '\n'
    return result.strip()

def raw_input(path, ignore_num=True):
    result = []
    with open(path, 'r') as inf:
        if ignore_num:
            inf.readline()
        casenew = True
        while True:
            if casenew:
                line = inf.readline()
                if not line.strip():
                    break
                line = line.strip().split()
                r = int(line[0])
                c = int(line[1])
                case = []
                casenew = False
            else:
                i = 0
                while i < r:
                    i += 1
                    line = inf.readline()
                    case.append(list(line.strip()))
                result.append(case)
                casenew=True
    return result

def run(input):
    i = 1
    for line in input:
        output = process(line)
        print "Case #%d:\n%s" % (i, str(output))
        i += 1

if __name__ == '__main__':
    run(raw_input(INFILE))
