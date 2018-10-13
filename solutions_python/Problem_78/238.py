'''
Created on 2011-5-21

@author: Cyanic
'''
fp = open('A-small-attempt4.in', 'r')
fpw = open('A-small-attempt4.out', 'w')

T = int(fp.readline())
ok = 0

for i in range(1,T + 1):
    three = fp.readline().split(" ")
    N = int(three[0])
    PD = int(three[1])
    PG = int(three[2])
    ok = 0
    if PD == 100 and PG != 0:
        fpw.write('Case #%d: Possible\n' % i)
        #print 'a'
        continue
    if PD == 0 and PG == 0:
        fpw.write('Case #%d: Possible\n' % i)
        #print 'a'
        continue
    if PG == 0 :
        fpw.write('Case #%d: Broken\n' % i)
        #print 'a'
        continue
    for j in range(1, min(N + 1, 101)):
        #intj = int(j * PD)
        if (j * PD) % 100 == 0 and PG != 100 :
            print j
            fpw.write('Case #%d: Possible\n' % i)
            ok = 1
            break
    if ok == 1:
        continue
    fpw.write('Case #%d: Broken\n' % i)
    print 0
    
    

