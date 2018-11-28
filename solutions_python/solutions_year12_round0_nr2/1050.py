import os
import sys

inputline = ""
ntestcases = 0
N = 0
S = 0
P = 0

r = 0
f = open("B-large.in","r")
g = open("output.out","w")

def getDisp(r):
	if(r==0) :
		return 1
	if(r==1) :
		return 1
	if(r==2) :
		return 2
		
ntestcases = int(f.readline())
j = 0
for line in f:
	j =j+1
	answer = 0
	arr = line.split(' ')
	N = int(arr[0])
	S = int(arr[1])
	P = int(arr[2])
	scores = arr[3:]
	
	#print scores
	i = 0
	for score in scores:
		scores[i] = int(score)
		i = i + 1
	
	for score in scores:
		q = int(score/3)
		r = score - q*3
		disp = getDisp(r)
		
		if( (q + disp) < P):
			continue
		if( (q >= P) ):
			answer = answer + 1
			continue
		if( (r==0) and q+1>=P and S>0 and q!=0):
			answer = answer +1
			S = S - 1
			continue
		if( (r == 1) and ((q + r) >= P) ):
			answer = answer + 1
			continue
		if( (r == 2) ):
			if( (q + 1) >= P):
				answer = answer + 1
				continue
			if( (q + 2) >= P and S>0):
				answer = answer + 1
				S = S - 1
				continue
	g.write("Case #"+str(j)+": "+str(answer)+"\n")

f.close()
g.close()
				
		
		
	
	
	
