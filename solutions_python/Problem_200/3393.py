# Copyright PM. April 2017
#!/usr/bin/python -tt


import sys
import random
import time
start_time = time.time()

def LastTidyNumber(N): 
	# Breaking down into digits.
	temp = N;
	while(temp>0):
		[tidy, index, lod ] = checktidy(temp)
		if (tidy):
			return temp;
		else:
			#print temp,x,pow(10,len(digits)-x-1)
			temp = int(temp/pow(10,lod-index-1))
			temp = temp*pow(10,lod-index-1) - 1
			#print temp
	return 0;
		 
def checktidy(N): 
	# Breaking down into digits.
	temp = N
	i = 0;
	digits = [];
	while(N>0):
		digits.append((N % 10));
		N = int(N/10);
		i = i + 1;
	digits = digits[::-1]; #reverse the list
	#print digits
	for x in xrange(len(digits)-1):
		if digits[x+1] < digits[x]:
			return 0,x,len(digits);
	
	return 1,0,0;
		 
def main():
  if len(sys.argv) < 2:
    print 'usage: ./tidynumber.py --filename'
    sys.exit(1)
	
  array = []
  filename = sys.argv[1] # This argument has filename argument
  #print filename

  with open(filename) as f:
    for line in f:
        data = line.split();
        array.append(int(data[0]));

  #print array
  T = array[0];
  casesN = array[1:T+1];
  caseind = 0;
  tidy = [];
  for N in casesN:
	  #print N;
	  tidy.append(LastTidyNumber(int(N)));
	  caseind = caseind + 1;

  #tidy,indx = checktidy(int(N)) 
  for i in xrange(T):
	  print 'Case #'+str(i+1)+': '+str(tidy[i])
 

if __name__ == '__main__':
  main()
  #print ("%s" % (time.time() - start_time))

