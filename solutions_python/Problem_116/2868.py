#author: AIVIN V. SOLATORIO
#loc: PHL


import sys

inp = open(sys.argv[1])
outp = file('tic-tac-toe-tomek.out', 'w')
lines = inp.read().split('\n')


numT = int(lines[0])

lines = lines[1:]


for i in xrange(numT):
    flag = 0
    countDots = 0
    #print lines
    start = i*4 + i
    T = lines[start:start + 5][:4]
    #horizontal check
    for j in T:
        countDots += j.count('.')
        #case 1: no T
        if ((j.count('X')==4) or (j.count('O')==4)):
            outp.write('Case #%s: %s won\n' % (i+1, j[0]))
            flag = 1
            break
        elif ((j.count('T')==1) and ((j.count('X')==3) or (j.count('O')==3))):
            try:
                outp.write('Case #%s: %s won\n' % (i+1, j[j.find('X')]))
                flag = 1
                break
            except:
                outp.write('Case #%s: %s won\n' % (i+1, j[j.find('O')]))
                flag = 1
                break

    if flag:
        continue

    #vertical check
    for k in xrange(4):
        print T
        j = [T[l][k] for l in xrange(4)]
        countDots += j.count('.')
        #case 1: no T
        if ((j.count('X')==4) or (j.count('O')==4)):
            outp.write('Case #%s: %s won\n' % (i+1, j[0]))
            flag = 1
            break
        elif ((j.count('T')==1) and ((j.count('X')==3) or (j.count('O')==3))):
            try:
                outp.write('Case #%s: %s won\n' % (i+1, j[j.index('X')]))
                flag = 1
                break
            except:
                outp.write('Case #%s: %s won\n' % (i+1, j[j.index('O')]))
                flag = 1
                break

    if flag:
        continue

    #diagonal check 1
    j = [T[l][k] for l, k, in zip(xrange(4), xrange(4))]
    countDots += j.count('.')
    #case 1: no T
    if ((j.count('X')==4) or (j.count('O')==4)):
        outp.write('Case #%s: %s won\n' % (i+1, j[0]))
        flag = 1
    elif ((j.count('T')==1) and ((j.count('X')==3) or (j.count('O')==3))):
        try:
            outp.write('Case #%s: %s won\n' % (i+1, j[j.index('X')]))
            flag = 1
        except:
            outp.write('Case #%s: %s won\n' % (i+1, j[j.index('O')]))
            flag = 1

    if flag:
        continue

    #diagonal check 2
    j = [T[l][k] for l, k, in zip(xrange(4), xrange(3,-1,-1))]
    countDots += j.count('.')
    #case 1: no T
    if ((j.count('X')==4) or (j.count('O')==4)):
        outp.write('Case #%s: %s won\n' % (i+1, j[0]))
        flag = 1
    elif ((j.count('T')==1) and ((j.count('X')==3) or (j.count('O')==3))):
        try:
            outp.write('Case #%s: %s won\n' % (i+1, j[j.index('X')]))
            flag = 1
        except:
            outp.write('Case #%s: %s won\n' % (i+1, j[j.index('O')]))
            flag = 1

    if flag:
        continue

    if countDots:
        outp.write('Case #%s: Game has not completed\n' % (i+1))
    else:
        outp.write('Case #%s: Draw\n' % (i+1))
