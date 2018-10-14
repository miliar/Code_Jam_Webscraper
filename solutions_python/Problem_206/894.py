#!/usr/bin/env python

INFILE='/Users/linlin/Downloads/A-large.in'
#INFILE='./test.txt'

def process(input):
    len = input[0]
    time = 0
    input = input[1:]
    for case in input:
        nt = (len - case[0])/ float(case[1])
        if nt > time:
            time = nt
    s = len / time
    return '%.6f' % s

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
                l = int(line[0])
                c = int(line[1])
                case = []
                case.append(int(l))
                casenew = False
            else:
                i = 0
                while i < c:
                    i += 1
                    line = inf.readline()
                    case.append(map(int, line.strip().split()))
                result.append(case)
                casenew=True
    return result

def run(input):
    i = 1
    for line in input:
        output = process(line)
        print "Case #%d: %s" % (i, str(output))
        i += 1

if __name__ == '__main__':
    run(raw_input(INFILE))
