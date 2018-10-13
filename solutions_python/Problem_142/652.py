#!/usr/bin/env python
#coding=utf-8
import copy, re

##inPath = 'test.in'
##outPath = 'test.out'
inPath = 'A-small-attempt0.in'
outPath = "A-small-attempt0.out"
##inPath = 'A-large.in'
##outPath = "A-large.out"

pattern = re.compile(r'(\w)(\1*)')
def count(ss, s_num):
    ss_i = copy.deepcopy(ss)
    ss_count = []
    for i in xrange(len(ss_i)):
        cou = pattern.findall(ss_i[i])
        c = []
        newss = ''
        for d, d1 in cou:
            newss += d
            c.append(1 + len(d1))
        ss_count.append(c)
        ss_i[i] = newss
    if len(set(ss_i)) != 1:
        return -1
    else:
        aver = []
        for col in xrange(len(ss_count[0])):
            aver.append(round(float(sum([ss_count[r][col] for r in xrange(s_num)])) / float(s_num)))
        tot = []
        for col in xrange(len(ss_count[0])):
            tot.append(int(sum([abs(ss_count[r][col] - aver[col]) for r in xrange(s_num)])))
        return sum(tot)

with open(outPath,'w') as outf:
    with open(inPath) as inf:
        n = int(inf.readline().strip())
        for case in xrange(1, n+1):
            ss = []
            s_num = n = int(inf.readline().strip())
            for i in xrange(s_num):
                ss.append(inf.readline().strip())
            res = count(ss, s_num)
            
            if -1 == res:
                outf.write("Case #" + str(case) + ": Fegla Won\n") 
            else:
                outf.write("Case #" + str(case) + ": " + str(res) + '\n')
    inf.close()
outf.close()
