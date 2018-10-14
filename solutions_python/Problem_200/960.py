#!/usr/bin/env python

#INFILE='./test.txt'
INFILE='/Users/linlin/Downloads/B-large.in'

def process(input):
    result = list(input)
    result = map(int, result)
    l = len(result)
    i = 0
    upd9 = l
    while i < l:
        if i >= upd9:
            result[i] = 9
            i+=1
            continue
        if (i+1) >= l:
            i += 1
            continue
        if result[i] <= result[i+1]:
            i += 1
        else:
            upd9 = i+1
            result[i] = result[i] - 1
            if (i-1) >= 0 and result[i] < result[i-1]:
                i -= 1
            else:
                i += 1
    result = ''.join(map(str, result)).strip('0') 
    return result

def raw_input(path, ignore_num=True):
    result = []
    with open(path, 'r') as inf:
        if ignore_num:
            inf.readline()
        for line in inf:
            result.append(line.strip())
    return result

def run(input):
    i = 1
    for line in input:
        output = process(line)
        print "Case #%d: %s" % (i, str(output))
        i += 1

if __name__ == '__main__':
    run(raw_input(INFILE))
