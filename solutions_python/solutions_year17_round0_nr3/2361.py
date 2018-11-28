# Copyright AN. April 2017
#!/usr/bin/python -tt


import sys
import random
import time
from math import log
start_time = time.time()

def assignuserfast(N,K): 
	# Breaking down into digits.
	BN = int(log(K,2))+1
	fac = 0;
	for x in xrange(BN-1):
		fac = fac + pow(2,x);
	#print BN,fac
	maxp = int((N-K+fac+1)/pow(2,BN));
	minp = int((N-K)/pow(2,BN));
	return maxp,minp

def assignuser(indexocc): 
	# Breaking down into digits.
	temp = indexocc
	maxdiff = 0;
	p1 = 0
	p2 = 0
	for x in xrange(len(indexocc)-1):
		diff = indexocc[x+1] - indexocc[x];
		#print diff
		if (maxdiff < diff):
			maxdiff = diff;
			[p1,p2] = [indexocc[x],indexocc[x+1]]
			[x1,x2] = [x,x+1]
	
	newpos = int(maxdiff/2) + p1
	indexocc.insert(x1+1,newpos); #(position,value)
	
	#print p1,p2,newpos
	#print indexocc
	ls = newpos - p1 -1;
	rs = p2 - newpos -1;
	return indexocc,max(ls,rs),min(ls,rs),newpos

		 
def main():
  if len(sys.argv) < 2:
    print 'usage: ./bathroomstalls.py --filename'
    sys.exit(1)
	
  array = []
  filename = sys.argv[1] # This argument has filename argument
  #print filename

  with open(filename) as f:
    for line in f:
        data = line.split();
        array = array + data; 

  #print array
  T = int(array[0]);
  #print T
  cases = array[1:];
  #print cases
  casesN = cases[0::2]
  casesK = cases[1::2]
  #print casesN
  #print casesK

  i = 0
  
  for i in xrange(T):

#	  indexocc = []
#  	  # assign guards at the end
#  	  indexocc.append(1);
#	  indexocc.append(int(casesN[i])+2);
#	  #print indexocc 
#	
#	  j = int(casesK[i]);
#	  while (j):
#		  [indexocc, maxp, minp,newpos] = assignuser(indexocc)
#		  j = j -1;
#
	  #print indexocc,newpos
	  [fmaxp,fminp] = assignuserfast(int(casesN[i]),int(casesK[i]))
	  #print 'Case C#'+str(i+1)+': '+str(maxp),str(minp)
	  print 'Case #'+str(i+1)+': '+str(fmaxp),str(fminp)
	  

#   caseind = 0;
#   tidy = [];
#   for N in casesN:
# 	  #print N;
# 	  tidy.append(LastTidyNumber(int(N)));
# 	  caseind = caseind + 1;
# 
#   #tidy,indx = checktidy(int(N)) 
#   for i in xrange(T):
# 	  print 'Case #'+str(i+1)+': '+str(tidy[i])
#  

if __name__ == '__main__':
  main()
  #print ("%s" % (time.time() - start_time))

