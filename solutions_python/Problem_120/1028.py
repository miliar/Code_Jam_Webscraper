'''
Problem
Maria has been hired by the Ghastly Chemicals Junkies (GCJ) company to help them manufacture bullseyes. 
A bullseye consists of a number of concentric rings (rings that are centered at the same point), 
and it usually represents an archery target. GCJ is interested in manufacturing black-and-white bullseyes. 

Maria starts with t millilitres of black paint, 
which she will use to draw rings of thickness 1cm (one centimetre). 
A ring of thickness 1cm is the space between two concentric circles whose radii differ by 1cm.

Maria draws the first black ring around a white circle of radius r cm. 
Then she repeats the following process for as long as she has enough paint to do so:

Maria imagines a white ring of thickness 1cm around the last black ring.
Then she draws a new black ring of thickness 1cm around that white ring.
Note that each "white ring" is simply the space between two black rings.
The area of a disk with radius 1cm is pi cm2. 
One millilitre of paint is required to cover area pi cm2. 
What is the maximum number of black rings that Maria can draw? Please note that:

Maria only draws complete rings. 
If the remaining paint is not enough to draw a complete black ring, she stops painting immediately.
There will always be enough paint to draw at least one black ring.

'''
import sys
from math import floor
#import itertools
#import threading
#threading.stack_size(2*67108864) # 64MB stack
#sys.setrecursionlimit(2 ** 20)
def ProblemA(InputFileName):
	#global
	OutputFileName=InputFileName.replace('.in','.out')
	lines = open(InputFileName).read().splitlines()
	#f1=open(InputFileName)
	f2=open(OutputFileName,'w')
	T=int(lines[0])
	for c in range(1, T+1):
		r,t=map(int,lines[c].split())
		r2=2*r-1;d=r2**2+8*t
		d2=int(d**0.5)
		while d2**2>d:
			print 'error';d2-=1
		#if d2**2!=float(d):print 'error'
		n=(d2-r2)/4
		# i=0
		# while t>0:
			# t-=2*r+1
			# i+=1
			# r+=2
		# if t!=0:i-=1
		print n#,d,d2**2#,i
		f2.write('Case #'+str(c)+': ' + str(n)+'\n')#, file=f) 
def main():	
	if len(sys.argv)==2: FileName=sys.argv[1]
	else: FileName='A-example.in'
	ProblemA(FileName)
# only new threads get the redefined stack size
# thread = threading.Thread(target=main)
# thread.start()
if __name__ == '__main__':
	main()