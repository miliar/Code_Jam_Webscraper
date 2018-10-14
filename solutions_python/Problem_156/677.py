import sys
import numpy as np
import math

infilename = sys.argv[1]
f=open(infilename,'r')
numlines = int(f.readline())

def totalTime(Ps,Splits):
	Eats = np.max(np.ceil(Ps/Splits))
	return Eats + np.sum(Splits-1.)

def bruteForce(f,numlines):
	for i in range(numlines):
		f.readline()
		Ps=np.array([float(p) for p in f.readline().split()])
		Splits=np.ones(len(Ps))
		time_initial = totalTime(Ps,Splits)
		for j in range(50000):
			Splits[np.where(np.ceil(Ps/Splits)==(np.ceil(Ps/Splits)).max())[0][0]]+=1.
			time_next = totalTime(Ps,Splits)
			if (time_next<time_initial):
				time_initial=time_next
	
		print "Case #"+str(i+1)+": "+str(int(time_initial))

def fartSmorce(f,numlines):
	for i in range(numlines):
		f.readline()
		Ps=np.array([float(p) for p in f.readline().split()])
		Splits=np.ones(len(Ps))
		time_initial = totalTime(Ps,Splits)
		Splits[np.where(Ps==Ps.max())[0][0]]+=1.
		time_next = totalTime(Ps,Splits)
		
		while time_next <= time_initial:
			time_initial=time_next
			Splits[np.where(np.ceil(Ps/Splits)==np.ceil(Ps/Splits).max())[0][0]]+=1.
			time_max = totalTime(Ps,Splits)	
			for j in range(6*9):
				Splits[np.where(np.ceil(Ps/Splits)==np.ceil(Ps/Splits).max())[0][0]]+=1.
				time_next = totalTime(Ps,Splits)
				if (time_next<=time_max):
					time_max=time_next
			time_next=time_max				
	
		print "Case #"+str(i+1)+": "+str(int(time_initial))

bruteForce(f,numlines)
#fartSmorce(f,numlines)

f.close()






