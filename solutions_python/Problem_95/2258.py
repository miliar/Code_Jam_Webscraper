#!/usr/bin/python2.7

import fileinput

flipList = ['  ', 'ay', 'bh', 'ce', 'ds', 'eo',
            'fc', 'gv', 'hx', 'id', 'ju',
            'ki', 'lg', 'ml', 'nb', 'ok',
            'pr', 'qz', 'rt', 'sn', 'tw',
            'uj', 'vp', 'wf', 'xm', 'ya', 'zq'
            ]
flipMap = dict([(a[0],a[1]) for a in flipList])

#de kr kd eoya kw aej tysr re ujdr lkgc jv
#so it is okay if you want to just give up

#rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
#there are twenty six factorial possibilities

#ejp mysljylc kd kxveddknmc re jsicpdrysi
#our language is impossible to understand

def flip(c):
    return flipMap[c]

def runTc(line):
    return "".join([flip(c) for c in line])

def main():
    lineCount = 0
    currTcNo = 0
    noOfTestCases = None
    for line in fileinput.input():
        if lineCount == 0:
            noOfTestCases = int(line)
        else:
            currTcNo += 1
            print "Case #%d: %s" % (currTcNo, runTc(line.strip()))

        lineCount += 1

if __name__ == '__main__':
    main()
