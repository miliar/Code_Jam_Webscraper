import os
import sys
from collections import deque
			
f = open("input.in","r")
g = open("output.out","w")
numtestcases = int(f.readline())

def getdigitarray(num):
	arr = []
	for n in str(num):
		arr.append(int(n))
	return arr
	
def getrotations(num):
	arr = []
	d = deque(getdigitarray(num))
	for i in range(0, len(str(num))):
		d.appendleft(d.pop())
		y = int(''.join(map(str,list(deque(d)))) )
		if(y!=num):
			arr.append( y )
	return arr

def solve(f,g):
	deq = []
	i = 0
	for line in f:
		i = i + 1
		print(line)
		answer = 0
		lower = int(line.split(" ")[0])
		upper = int(line.split(" ")[1])
		if(lower>upper):
			answer =  0
		
		a = range(lower,upper+1)
		lolmaxarr = []
		for num in a:
			#print "\tnumber : ",num
			digitsArr = getrotations(num)
			#print "\t",digitsArr
			
			for x in digitsArr:
				if (x >= lower and x<=upper) and x!=num:
					
					print "(",num,x,")"
					pair = ""
					
					if(x>num):
						pair = str(num)+str(x)
					else:
						pair = str(x)+str(num)
						
					if pair not in lolmaxarr:
						lolmaxarr.append(pair)
						answer = answer + 1
									 
		print "Answer : ",answer
		#raw_input("Next line...")
		g.write("Case #"+str(i)+": "+str(answer)+"\n")
		

solve(f,g)
		
f.close()
g.close()