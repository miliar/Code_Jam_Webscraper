#
# Google Code Jam 2011
# Roaund 0: B. Magicka
# submission by EnTerr
#

'''
Input 
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
	
Output 
Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []
'''

import sys
#import psyco
#psyco.full()

f = open(sys.argv[1])
def input(): return f.readline().strip();


def magicka(it):
    # 1 EEZ 1 QE 7 QEEEERA
    combine = {}
    for _ in range(int(it.next())):
        s = it.next()
        combine[s[0],s[1]] = s[2:]
        combine[s[1],s[0]] = s[2:] # reverse is also true

    oppose = {}
    for _ in range(int(it.next())):
        s = it.next()
        oppose[s[0]] = s[1]
        oppose[s[1]] = s[0]

    it.next() # skip
    
    mgk = [''] # empty stack but need at least 1 element
    for elem in it.next():
        if (mgk[-1],elem) in combine:
            mgk[-1] = combine[mgk[-1],elem]
        elif (elem in oppose) and (oppose[elem] in mgk):
            # flush the stack
            mgk = ['']
        else:
            mgk.append(elem)
    
    return ', '.join(mgk[1:])





for caseNo in range(1, int(input())+1):
    print 'Case #%d: [%s]' % (caseNo, magicka( iter(input().split()) ))

