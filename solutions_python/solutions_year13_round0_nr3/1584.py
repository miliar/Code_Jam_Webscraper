from sys import argv
import sys
from itertools import cycle

in_file = argv[1]

def is_square(pint):
  if pint == 1:
     return True
  x = pint // 2
  seen = set([x])
  while x * x != pint:
   x = (x + (pint // x)) // 2
   if x in seen: return False
   seen.add(x)
  return True

def mysqrt(n):
   xn = 1
   xn1 = (xn + n/xn)/2
   while abs(xn1 - xn) > 1:
     xn = xn1
     xn1 = (xn + n/xn)/2
   while xn1*xn1 > n:
     xn1 -= 1
   return xn1

def mypal(n):
   tmp = str(n)[::-1]
   if tmp == str(n):
     return True
   else:
     return False
     
with open(in_file) as f:
        cases = int(f.readline())
        #cases = 1 #tmp
        mylist = []
        #for case in range(cases):
        #A,B = [int(x) for x in f.readline().split()]
	ans = 0
	#print "Case #%d:" % (case+1)
	#print "A: ",A,", B: ",B
	A = 1
	B = 100000000000000
	#for i in range(A,B+1):
	flag = False
	while flag == False:
	  if (is_square(A) == True):
	     flag = True
	  else:
	     A += 1

	mysq = mysqrt(A)
	while A <= B:
	   i = A
	   #A += 1
	   #print "i: %d"%i
	   #if (mypal(i) == True) and (is_square(i) == True):
	   '''
	   if (mypal(i) == True):
	      if mysq == 0:
		 mysq = mysqrt(i)
	      if ((mypal(mysq)) == True):
		 ans += 1
	   '''
	   
	   if (mypal(mysq) == True) and (mypal(i) == True):
	       ans += 1
	       #print "[%d] - [%d]"%(i,mysq)
	       mylist.append(i)
	   A = A + (2*mysq) +1
	   mysq = mysq + 1
	#print "Case #%d: %d"%((case+1),ans)

        
	for case in range(cases):
	    ans = 0
	    A,B = [int(x) for x in f.readline().split()]
	    for num in mylist:
	         if num >= A and num <= B:
	            ans += 1
	            #print "Num: %d"%num
	    print "Case #%d: %d"%((case+1),ans)
		

