#!/usr/bin/env python

INFILE='/Users/linlin/Downloads/C-large.in'
#INFILE='./test.txt'

def process(input):
    n, k = input.split()
    n = int(n)
    k = int(k)
    while k > 1:
        if n % 2 ==1:
            n = (n -1)/2
            if k % 2 == 1:
                k = (k - 1)/2
            else:
                k = k / 2
        else:
            if k % 2 == 1:
                n = n/2 - 1
                k = (k - 1) /2
            else:
                n = n/2
                k = k /2
    if n % 2 == 1:
        l = (n -1)/2
        r = l
    else:
        l = n/2
        r = l - 1
    result = '%d %d' % (l, r)
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
