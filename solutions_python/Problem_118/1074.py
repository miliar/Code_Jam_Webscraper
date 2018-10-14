from __future__ import print_function, division

from bisect import bisect_left
import sys
import math

infile = open(sys.argv[1])
outfiles = (sys.stdout, open(sys.argv[2], 'w'))

def read_in(infile):
    data = infile.readlines()
    amount = int(data[0])
    content = data[1:]
    assert amount == len(content)
    return [s.strip() for s in content]

def do_output(number, output, outfiles):
    for f in outfiles:
        print('Case #%d:' % number, output, file=f)

def main():
    for i, content in enumerate(read_in(infile)):
        do_output(i+1, do_task(content), outfiles)


def do_task(content):
    # Parse input string
    limits = [int(math.sqrt(int(x))) for x in content.split()]
    if(limits[0]*limits[0] < int(content.split()[0])):
        limits[0] += 1
    count = 0
    for i in range(limits[0], limits[1]+1):
        s = str(i)
        if(s == s[::-1]):
            t = str(i*i)
            if(t == t[::-1]):
                #print(i)
                count+=1
    return str(count)

if __name__=='__main__':
    main()
