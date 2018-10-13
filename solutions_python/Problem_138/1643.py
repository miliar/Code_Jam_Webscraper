# !/usr/bin/env python

from sys import stdin

T = int(stdin.next().strip())
fout = open('large.out','w')
def outrange(a,b):
    for i in xrange(len(a)):
	if a[i]<b[i]:
	    return 0
	else:
	    continue
    return 1

for i in xrange(T):
    print '#########################Game',i+1
    num = int(stdin.next().strip())
    n = sorted(map(float,stdin.next().strip().split()))
    k = sorted(map(float,stdin.next().strip().split()))
    ##War Game 
    nWin=0
    kWin=0
    nOrgin=n[:]
    kOrgin=k[:]
    for j in xrange(num):
	nCh=n[j]
	temp = [x for x in kOrgin if x>nCh]
	nOrgin.remove(nCh)
	if len(temp)==0:
	    kOrgin.remove(min(kOrgin))
	    nWin += 1
	else:
	    kOrgin.remove(min(temp))
	    kWin +=1
    print 'nwin',nWin 

    #Deceitful War
    nDec=n[:]
    kDec=k[:]
    nDeWin = 0
    for j in xrange(num):
	if outrange(nDec,kDec):
	    if i==2:
		print nDec,kDec
		print outrange(nDec,kDec)
	    nDeWin = num-j
	    break
	else:
	    nDec.remove(min(nDec))
	    kDec.remove(max(kDec))
	
    print 'nDeWin',nDeWin

    print>>fout,'Case #%d: %d %d' %(i+1,nDeWin,nWin)

fout.close()
