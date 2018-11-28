import fileinput

fi = fileinput.input()

def makePalList(NdigMax):
   ns = []
   for n in xrange(1,10):
      ns.append(n)
   ms = []
   for m in xrange(10):
      ms.append(str(m))
   currD = 2
   symmPal = [str(n)+str(n) for n in ns]
   palindromes = ns[:]
   for sp in symmPal:
      palindromes.append(int(sp))
   while(currD<=NdigMax):
      currD+=2
      newSymL = []
      for sym in symmPal:
        lp = len(sym)
        half1 = sym[:lp/2]
        half2 = sym[lp/2:]
        for m in ms:
          palindromes.append(int(half1+m+half2))
	for m in ms:
          palindromes.append(int(half1+m+m+half2))
          newSymL.append(half1+m+m+half2)
      symmPal=newSymL
   return palindromes

def checkP(p):
   ps = str(p)
   lp = len(ps)
   half1 = ps[:lp/2]
   half2 = ps[lp/2:]
   symm = True
   for i in xrange(len(half1)):
      if half1[i] != half2[-1-i]: 
        symm = False
        break
   return symm

def cleanPalList(pl):
   cleanList = []
   for p in pl:
     pn=int(p)
     if checkP(pn*pn): cleanList.append(pn)
   return cleanList

plist = makePalList(7)
cleanList = cleanPalList(plist)
#print cleanList
T = int(fi.readline())
for case in xrange(T):
   A,B = map(int, fi.readline().strip().split())
   count = 0
   A = A**0.5
   B = B**0.5
   for cp in cleanList:
     if A<=cp<=B: count+=1
   print 'Case #'+str(case+1)+': '+str(count)

