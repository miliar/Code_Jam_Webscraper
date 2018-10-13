#!/usr/bin/python
import sys
import re

def main():
    f = open(sys.argv[1])
    (l, d, n) = f.readline().split()
    #print l,d,n
    l = int(l)
    d = int(d)
    n = int(n)

    slang = []
    dlang = []
    for i in range(d):
        slang.append(f.readline())
    for i in range(n):
        dlang.append(f.readline())

    #print slang, dlang

    dlang2 = []
    for i in dlang:
        dlang2.append(re.compile('^'+i.replace('(','[').replace(')',']').replace('\n','$')))
    #print dlang2

    for n,i in enumerate(dlang2):
        m = 0
        for k in slang:
            result = i.findall(k)
            if len(result) != 0:
                m += 1
        print 'Case #%d: %d' % (n+1, m)





if __name__ == '__main__':
    main()
