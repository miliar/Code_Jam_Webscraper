#!/usr/bin/python

for case in range(input()):
    T = int(raw_input())
    A, B = map(int, raw_input().split())
    salA = []
    llegA = []
    for train in range(A):
        sal, lleg = raw_input().split()
        hour, min = map(int, sal.split(':'))
        salA.append(hour*60 + min)
        hour, min = map(int, lleg.split(':'))
        llegA.append(hour*60 + min + T)
    salB = []
    llegB = []
    for train in range(B):
        sal, lleg = raw_input().split()
        hour, min = map(int, sal.split(':'))
        salB.append(hour*60 + min)
        hour, min = map(int, lleg.split(':'))
        llegB.append(hour*60 + min + T)

    i = 0
    salB1 = []
    salB1.extend(sorted(salB))
    for time1 in sorted(llegA):
        while (i < len(salB1)) and (time1 > salB1[i]):
            i += 1
        if (i < len(salB1)): salB1.remove(salB1[i])
        if (i == len(salB1)): break

    i = 0
    salA1 = []
    salA1.extend(sorted(salA))
    for time1 in sorted(llegB):
        while (i < len(salA1)) and (time1 > salA1[i]):
            i += 1
        if (i < len(salA1)): salA1.remove(salA1[i])
        if (i == len(salA1)): break
    
    print 'Case #%s: %s %s' % (case + 1, len(salA1), len(salB1))
    
      
        
    
