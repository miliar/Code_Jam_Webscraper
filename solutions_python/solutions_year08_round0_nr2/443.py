#!/usr/bin/python
import sys
from time import strptime
from datetime import datetime,timedelta


class Train:
	def __init__(self):
		self.readyTime=datetime(2000,1,1,hour=0,minute=0)
	

def ReadInput():
	f=sys.stdin.readlines()
	data={}
	N=int(f[0])
	i=1
	for x in range(0,N):		
		T=int(f[i])
		NA,NB=f[i+1].split(" ")
		NA=int(NA)
		NB=int(NB)
		NAD=[]
		NBD=[]
		i=i+2
		for y in range(0,NA):
			NAD.append(f[i])
			i=i+1
		for z in range(0,NB):
			NBD.append(f[i])
			i=i+1
		data[x]=(T,NAD,NBD)
	return data

def SelectTrain(station,startTime):
	for t in station:
		if t.readyTime <= startTime:
			station.remove(t)
			return t
	return None 
	
	
def ProcessTrains(t,NAD,NBD):
		results=[]
		AStation=[]
		BStation=[]
 		NAD.sort()
		NBD.sort()
		Depart = [(x,0) for x in NAD] + [(x,1) for x in NBD]
		Depart.sort()
		delta = timedelta(minutes=t)
		for x in range(0,len(NAD)+1):
			for y in range(0,len(NBD)+1):
				passed=1
				AStation=[]
				BStation=[]
				for t in range(0,x):
					AStation.append(Train())
				for t in range(0,y):
					BStation.append(Train())
				for z in Depart:
					temp=z[0].strip()
					s,f = temp.split(" ")
					temp = strptime(s,"%H:%M")
					startTime = datetime(2000,1,1,hour=temp[3],minute=temp[4])
					temp = strptime(f,"%H:%M")
					endTime = datetime(2000,1,1,hour=temp[3],minute=temp[4])
					if z[1]==0:
						train = SelectTrain(AStation,startTime)
						#print z,0,train,x,y
						if train == None:
							passed = 0
							break
						train.readyTime = endTime + delta
						BStation.append(train) 
					else:
						train = SelectTrain(BStation,startTime)
						#print z,1,train,x,y
						if train == None:
							passed = 0
							break
						train.readyTime = endTime + delta
						AStation.append(train)
				if passed:
					results.append((x,y))
		
		results = [(x+y,(x,y)) for x,y in results] 	
		results.sort()
		return results[0][1]
					
					
			
											
				
			
	
if __name__ == "__main__":
	data = ReadInput()
	for x in range(0,len(data)):
		a,b = ProcessTrains(data[x][0],data[x][1],data[x][2])
		print "Case #%d: %d %d" % (x+1,a,b)