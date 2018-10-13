#!/usr/bin/env python

line = []
#for l in open('sample', 'r'):
for l in open('A-large.in', 'r'):
    l = l.rstrip('\n')
    line.append(l)

N = int(line[0])

for i in range(N):
    Bsch = []
    Osch = []
    n = ''
    l = line[i + 1].split(' ')
    l.pop(0)
    s = 0
    for p in l:
        s += 1
        if (p == 'B'):
            n = p
        elif (p == 'O'):
            n = p
        elif (n == 'B'):
            Bsch.append([int(p), s])
            n = ''
        elif (n == 'O'):
            Osch.append([int(p), s])
            n = ''

    T = 0
    Bpos = 1
    Opos = 1
    while (len(Bsch) > 0 or len(Osch)):
        T += 1
        pushed = False
        if len(Bsch) > 0:
            if Bpos == Bsch[0][0]:
                if (len(Osch) == 0 or Bsch[0][1] < Osch[0][1]):
                    # push button
                    Bsch.pop(0)
                    pushed = True
            else:
                # move
                if Bpos > Bsch[0][0]:
                    Bpos -= 1
                else:
                    Bpos += 1
        if len(Osch) > 0:
            if Opos == Osch[0][0]:
                if (len(Bsch) == 0 or Osch[0][1] < Bsch[0][1]) and not pushed:
                    # push button
                    Osch.pop(0)
            else:
                # move
                if Opos > Osch[0][0]:
                    Opos -= 1
                else:
                    Opos += 1
    print 'Case #%d: %d' % (i + 1, T)
    del Bsch
    del Osch


