import sys
import re

words = []

#f = open('q1test.in', 'rU')
#fout = open('q1test.out', 'w')
f = open('A-small-attempt1.in', 'rU')
fout = open('A-small-attempt1.out', 'w')

def recurse(currword, line, pos):
    total = 0
    #if section of currword not matching to any in list, return
    exists = 0
    for i in words:
        if currword == '':
            exists = 1
            break
        if currword == i[:len(currword)]:
            exists = 1
            break
    if exists == 0: return 0

    if pos >= len(line):
        #print currword
        if currword in words: return 1
        else: return 0

    if line[pos] == '(':
        for i in range(pos+1, len(line)):
            if line[i] == ')':
                endpos = i
                break
        for i in range(pos+1, endpos):
            newcword = currword
            newcword += line[i]
            total += recurse(newcword, line, endpos+1)
    else:
        newcword = currword
        newcword += line[pos]
        total += recurse(newcword, line, pos+1)

    return total

length, nvalid, ncases = f.readline().strip().split()
length = int(length)
nvalid = int(nvalid)
ncases = int(ncases)

for i in range(nvalid):
    words.append(f.readline().strip())

words.sort()

for i in range(ncases):
    line = f.readline().strip()
    nwin = recurse('', line, 0)
    outstr = 'Case #'+str(i+1)+': '+str(nwin)+'\n'
    #print outstr
    fout.writelines(outstr)