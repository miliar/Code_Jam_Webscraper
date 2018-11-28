#!/usr/bin/python
import sys

def main():
    f = file(sys.argv[1])
    num = int(f.readline())
    #print 'num: ', num

    for i in range(num):
        line = f.readline()
        print "Case #%d: %s" % (i+1, trans(line))


def trans(line):
    if len(line) == 1:
        return 1
    n = line.strip('\n')
    ret = {}
    ret[n[0]] = 1
    beg = 0
    for i,j in enumerate(n[1:len(n)]):
        if j not in ret:
            ret[j] = beg
            if beg == 0:
                beg +=2
            else:
                beg += 1

    base = len(ret)
    if base < 2:
        base = 2
    ret2 = 0
    #print n,ret
    for i in n:
        ret2 = base*ret2 + ret[i]

    return ret2






    

if __name__ == '__main__':
    main()
