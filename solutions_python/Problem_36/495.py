import sys
import re

words = 'welcome to code jam'
line = ''

f = open('C-small-attempt2.in', 'rU')
fout = open('C-small-attempt2.out', 'w')
#f = open('test.in', 'rU')
#fout = open('test.out', 'w')


def recurse(indexstr, indexcj):
    total = 0
    while indexstr < len(line) and indexcj < len(words) and line[indexstr] != words[indexcj]:
        indexstr += 1
    if indexstr >= len(line) or indexcj >= len(words): return 0

    total += recurse(indexstr+1, indexcj+1)
    total += recurse(indexstr+1, indexcj)

    if line[indexstr] == 'm' and indexcj == len(words)-1: total += 1

    return total

ncase = int(f.readline().strip())

for i in xrange(ncase):
    line = f.readline().strip()
    #print line
    #matches = re.findall('w.*e.*l.*c.*o.*m.*e.* .*t.*o.* .*c.*o.*d.*e.* .*j.*a.*m', line)
    #print matches
    matches = recurse(0, 0)
    #print matches
    outstr = 'Case #%d: %04d\n' % (i+1, matches)
    #print outstr
    fout.writelines(outstr)