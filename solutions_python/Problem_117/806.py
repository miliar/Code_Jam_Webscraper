from __future__ import print_function, division

from bisect import bisect_left

import sys

infile = open(sys.argv[1])
outfiles = (sys.stdout, open(sys.argv[2], 'w'))

def read_in(infile):
    data = infile.readlines()
    data = [s.strip() for s in data]
    amount = int(data[0])
    content = []
    l = 1
    for i in range(0,amount):
        n,m = [(int) (x) for x in data[l].split(' ')]
        content.append(data[l+1:l+n+1])
        l+=n+1
    assert amount == len(content)
    return content

def do_output(number, output, outfiles):
    for f in outfiles:
        print('Case #%d: ' % number, output, file=f)

def main():
    for i, content in enumerate(read_in(infile)):
        do_output(i+1, do_task(content), outfiles)



def do_task(content):
    content = [s.split() for s in content]
    maxrow = [0]*len(content)
    maxcol = [0]*len(content[0])
    for n in range(0,len(content)):
        for m in range(0,len(content[0])):
            if(int(content[n][m]) > maxrow[n]):
                maxrow[n] = int(content[n][m])
            if(int(content[n][m]) > maxcol[m]):
                maxcol[m] = int(content[n][m])
    for n in range(0,len(content)):
        for m in range(0,len(content[0])):
            if(int(content[n][m]) != maxrow[n] and int(content[n][m]) != maxcol[m]):
                return 'NO'
    return 'YES'

if __name__=='__main__':
    main()
    #read_in(infile)
