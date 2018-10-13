import os
import sys
import time
sys.setrecursionlimit(10000)

class timeObj:
	def __init__(self,second):
		self.value=second

class station:
	def __init__(self,timeList=[],turnOverTime=0,name=''):
		self.name=name
		self.needed=0
		self.members=0
		self.turnOverTime=turnOverTime*60
		self.timeList=[]
		self.arriveList=[]
		self.addTime(timeList)

	def getNeeded(self):
		return self.needed

	def inTransit(self,arriveList):
		self.arriveList+=arriveList

	def addTime(self,timeList):
		for depart,arrive in timeList:
			depart=self.convertTime(depart)
			arrive=self.convertTime(arrive)
			self.timeList.append([depart,arrive])
		return 1

	def convertTime(self,value):
		HH,MM=value.split(":")
		seconds=3600*int(HH) + 60*int(MM)
		#print "%s == %s" % (value,seconds)
		return timeObj(seconds)

	def depart(self):
		if self.members:
			self.members-=1
			self.log("member %s" % self.members)
		else:
			self.needed+=1
			self.log("needed %s" % self.needed)
	def arrive(self):
		self.members+=1

	def log(self,text):
		pass
		#print "%s %s" % (self.name,text)

	def checkTime(self,timer):
		otherTimes=[]
		for arrive in list(self.arriveList):
			if (arrive.value+self.turnOverTime) ==timer:
				self.log("ARRIVE %s" % timer)
				self.arrive()
				self.arriveList.remove(arrive)
		for depart,arrive in list(self.timeList):
			if depart.value == timer:
				self.log("DEPART %s" % timer)
				self.depart()
				otherTimes.append(arrive)
				#print self.timeList
				self.timeList.remove([depart,arrive])

		#for arrive in list(self.arriveList):
		#	if (arrive.value+self.turnOverTime) ==timer:
		#		self.log("ARRIVE %s" % timer)
		#		self.arrive()
		#		self.arriveList.remove(arrive)
		return otherTimes
				



class parser:
	def __init__(self):
		self.MAXTIME=3600*24
		pass

	def run(self,naList,nbList,T):
		A=station(naList,T,'A')
		B=station(nbList,T,'B')

		second=0
		while second < self.MAXTIME:

			transit=A.checkTime(second)
			if transit:
				B.inTransit(transit)

			transit=B.checkTime(second)
			if transit:
				A.inTransit(transit)

			second+=1

		print "A %s" % A.getNeeded()
		print "B %s" % B.getNeeded()
		return A.getNeeded(),B.getNeeded()


	def parse(self,filename):
		result=[]
		data=file(filename,'r').readlines()
		print len(data)
		N=int(data[0].strip())
		n=1
		i=1
		while n <= N:
			T=int(data[i])
			i+=1
			NA,NB=data[i].split()
			na=0
			naList=[]
			nb=0
			nbList=[]
			while na < int(NA):
				i+=1
				naList.append(data[i].split())
				na+=1
			while nb < int(NB):
				i+=1
				nbList.append(data[i].split())
				nb+=1
			#if n != -1:
			print "N: %s" % N
			print "T: %s" % T
			print "n: %s" % n
			a,b=self.run(naList,nbList,T)
			result.append("Case #%s: %s %s" % (n,a,b))
			print "DONE"
			i+=1
			n+=1
			#print "N: %s" % N
			#print "T: %s" % T
			#print "NA: %s" % NA
			##print "NALIST: %s" % naList
			#print "NB: %s" % NB
			#print "NBLIST: %s" % nbList
		return result


if __name__ == "__main__":
	filename=sys.argv[1]
	outfilename=sys.argv[2]
	start=time.time()
	print time.ctime()
	a=parser()
	result=a.parse(filename)
	print "\n".join(result)
	print "Written to %s" % outfilename
	file(outfilename,'w').write("\n".join(result))
	end=time.time()
	print (end - start)
	print time.ctime()
	#for key,item in a.queryData.items():
	#	print "final %s %s" % (key,a.recurse(a.queryData[key]))
#	print a.queryData
#	print len(a.queryData[1])
#	print a.searchEngines

