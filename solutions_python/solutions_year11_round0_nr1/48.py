import string
import time

infile = open('a.in','r')
outfile = open('a.out','w')

T = int(string.strip(infile.readline()))

for i in xrange(T):
    s = string.split(string.strip(infile.readline()))
    N = int(s[0])
    s = s[1:]
    t = 0
    B_pos = 1
    O_pos = 1
    B_target = 1
    O_target = 1
    if s.count('O') > 0:
        O_target = int(s[s.index('O')+1])
    if s.count('B') > 0:
        B_target = int(s[s.index('B')+1])
    while len(s) > 0:
#        print 'O is at %d, target %d; B is at %d, target %d' % (O_pos,O_target,B_pos,B_target)
 #       print s
        pushed = False
        if O_pos != O_target:
            if O_pos > O_target:
                O_pos -= 1
            else:
                O_pos += 1
        elif s[0] == 'O':
 #           print 'O pushes button %d'% O_pos
            if s[2:].count('O') > 0:
                O_target = int(s[2:][s[2:].index('O')+1])
 #               print 'O now has target %d' % O_target
            pushed = True

        if B_pos != B_target:
            if B_pos > B_target:
                B_pos -= 1
            else:
                B_pos += 1
        elif s[0] == 'B':
            if s[2:].count('B') > 0:
                B_target = int(s[2:][s[2:].index('B')+1])
            pushed = True

        if pushed:
            s = s[2:]
        t += 1
    outfile.write('Case #%d: %d\n' % (i+1,t))
