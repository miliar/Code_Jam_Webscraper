#!/usr/bin/python
#
# author: tzeng.yuxio@gmail.com
# usage: cat file.input | ./qround-problem-a.py > file.output

import sys

strs = []

def short(s):
    rs = ""
    counts = []
    cc = 0
    for c in s:
        if len(rs) == 0:
            rs += c
            cc = 1
        elif c != rs[-1]:
            counts.append(cc)
            rs += c
            cc = 1
        else:
            cc += 1
    counts.append(cc)

    return rs, counts

def solve():
    strs = []
    szs = []
    n = int(sys.stdin.readline())
    for i in range(n):
        strs.append(sys.stdin.readline()[:-1])

    target, tmp = short(strs[0])
    tsz = len(target)
    for i in range(tsz):
        szs.append([])

    for i in range(n):
        if i == 0:
            ct, ccnt = short(strs[i])
            for j in range(tsz):
                # print j, tsz, ccnt
                szs[j].append(ccnt[j])
            # szs.append(len(strs[i]) - tsz)
        else:
            ct, ccnt = short(strs[i])
            if ct != target:
                return "Fegla Won"
            else:
                # szs.append(len(strs[i]) - tsz)
                for j in range(tsz):
                    # print j, tsz, ccnt
                    szs[j].append(ccnt[j])

    # r = sum(szs)
    # avg = round(r / float(len(szs)))
    r = 0
    for i in range(tsz):
        avg = int(round(sum(szs[i]) / float(len(szs[i]))))
        abl = [abs(avg - x) for x in szs[i]]
        r += sum(abl)

    # for i in range(len(szs)):
        # print str(szs[i])

    # return (strs)
    # return str(szs)
    return str(r)


t = (int)(sys.stdin.readline())
for i in range(t):
    print 'Case #' + repr(i+1) + ': ' + solve()
