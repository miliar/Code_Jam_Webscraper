# !/usr/bin/env python

from sys import stdin

T = int(stdin.next().strip())
fout = open('output.out','w')

for i in xrange(T):
    row1 = int(stdin.next().strip())
    sq1 = []
    for j in xrange(4):
	temp = stdin.next().strip().split()
	sq1.append(temp)

    row2 = int(stdin.next().strip())
    sq2 = []
    for j in xrange(4):
	temp = stdin.next().strip().split()
	sq2.append(temp)

    match=[x for x in sq1[row1-1] if x in sq2[row2-1]]
    
    if len(match)==1:
	out = int(match[0])
    elif len(match)>1:
	out = 'Bad magician!'
    elif len(match)==0:
	out = 'Volunteer cheated!'

    print>>fout,'Case #%d: %s' %(i+1,out)
    print 'Case #%d: %s' %(i+1,out)

fout.close()
