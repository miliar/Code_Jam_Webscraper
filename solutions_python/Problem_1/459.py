import os
import sys
import time

class parser:
	def __init__(self):
		self.deep=0
		self.next=0
		self.dataLength=0
		self.lost=[]
		self.lookup={}
		self.shortSwitch=9999
		self.cache=0
		self.almostcache=0
		self.nocache=0
		self.dup=0
		self.ugh={}
		self.least=99999
	def debug(self,data,blah):
		if len(data) == 100:
			print "DEBUG: %s" % str(blah)
			#raw_input()
	
	def recurse(self,S,Q,switches=0):

		for q in Q:
			for s in S:
				if q == s:
					switch+=1

	def recurse(self,data,i=0,switches=99999,count=0,searchengines=[],start=False,lookup=False):
		#print "CALL i %s" % i
		#self.debug(data,"start")
		#self.debug(data,len(data))
		#if self.lookup.has_key(i):
		#	return self.lookup[i]
		if count >= switches:
		#	print 'count'
			return count
		key2=str(i)
		if lookup == 'yes':
			if self.lookup.has_key(key2):
				if self.lookup[key2] < switches:
					#print key2,switches
					return self.lookup[key2]
				#else:
				#	self.lookup[key2]=switches
		for engine in searchengines:
			#if start:
				#print 'engine start %s' % engine
				#print self.lookup
			#print [engine]
			#time.sleep(.1)
			x=i
			key=engine+str(i)
			#print switches
			if lookup:# == 'yes':
				if self.lookup.has_key(key):
					#switches=self.lookup[key]
					self.almostcache+=1
					if self.lookup[key] < switches:
						self.cache+=1
						switches=self.lookup[key]
						continue
				self.nocache+=1
						#switches
					#else:
					#	self.lookup[key]=switches
					#	continue
					#return switches
			#print x
			#print data
			#time.sleep(.4)
			while (x<self.dataLength) and (engine != data[x]): 
				#print "[%s][%s] C%s x: %s" % (engine.strip(),data[x].strip(),count,x)
				#print "x+ %s" % x
				#self.debug(data,"loop %s" % x)
				#if engine == data[x]:
				#	#do something
				#	break
				#else:
				#self.debug(data,x)
				if x+1 < self.dataLength:
					if data[x+1] == engine:
						break
				x+=1
			#self.debug(data,(x,len(data),switches,self.deep,len(searchengines)))
			#bkey=str(x+1)+str(count+1)
			if x+1 >= self.dataLength:
				bkey=str(x)+str(count)
				switch=count
				self.ugh[bkey]=switch#.has_key(bkey):# and lookup:
				if self.least > switch:
					#print 'set %s' % switch
					#raw_input()
					self.least=switch
				#print 'max'
				#switch=count
					#print "COUNT %s %s %s" % (x,count,switch)
					#raw_input()
			else:
				#newKey=engine+str(x+1)
				#if self.lookup.has_key(newKey) and lookup:
				#	if self.lookup[newKey] < switches:
				#		self.cache+=1
				#		switches=self.lookup[newKey]
				#		continue
				#self.deep+=1
				#print 'call'
				#if self.deep >= self.next:
				#	self.next+=50000
					#print self.deep
				#print self.deep
				#print "COUNT CALL %s %s" % (count,x)
				bkey=str(x)+str(count)
				if self.ugh.has_key(bkey) and lookup:
					#print 'ugh'
					switch=self.ugh[bkey]
				else:
					#no change in count
					#if i == x:
					switch=self.recurse(data,x+1,count=count+1,searchengines=searchengines,lookup=lookup)
					#else:
					#	switch=self.recurse(data,x+1,count=count+1,searchengines=searchengines,lookup=lookup)

					self.ugh[bkey]=switch
				#print "GOT %s" % switch
				#if not self.lookup.has_key(key):
				#	self.lookup[key]=switch
				#else:
				#	if self.lookup[key] < switch:
				#		self.lookup[key]=switch
			#		pass
					#print 'hey %s  %s' % (self.lookup[key],switch)
			#self.lookup[key]=switch
				#print "KEY make %s" % key
			if switch <= switches:
				switches=switch
		#self.lookup[count]=switches
		if self.lookup.has_key(key):
			if self.lookup[key] == switches:
				self.dup+=1
		self.lookup[key]=switches
		if self.lookup.has_key(key2):
			if self.lookup[key2] > switches:
				self.lookup[key2]=switches
		else:
			self.lookup[key2]=switches
		#print self.lookup.keys()
		return switches

	def countSets(self,target,queryData):
		inSet=0
		total=0
		for item in queryData:
			if (item != target) and inSet:
				inSet=0
				total+=1
			elif item == target:
				inSet+=1
		if inSet:
			total+=1
			
		return total
	def findLeast(self,searchEngines,queryData):
		least=len(queryData)
		for s in searchEngines:
			count=self.countSets(s,queryData)#queryData.count(s)
			print s,count
			if count < least:
				least=count
		return least




	def findSegs(self,table,S):
			
		col=0
		for colName in S:
			i=0
			weight=0
			while i < len(table):
				try:
					x=int(table[i][col])
				except IndexError:
					print 'break'
					break
				if x == 0:
					weight+=1
				else:
					if weight:
						print "%s weight: %s" % (col,weight)
					weight=0
				i+=1
			col+=1

		return
		i=0
		dataSets=[]
		setLen=0
		while i < len(S):
			row=0
			while row < len(table):
				try:
					data=table[row][i]
				except IndexError:
					break
				if data == 0:
					setLen+=1
				else:
					if setLen:
						dataSets.append([setLen,i])
					setLen=0
				row+=1
			i+=1

		print dataSets


	def goTable(self,table,switch=0,i=0):
		if not table:
			return
		if switch >= self.shortSwitch:
			return
		for row in table:
			colSwitch=switch
			for col in table:
				if col != 0:
					switch+=1
					self.goTable(table[i:],switch,i)
			
			i+=1
		if switch < self.shortSwitch:
			self.shortSwitch=switch
		

	def makeTable(self,S,Q):
		new=[]
		#print "Q %s" % Q
		#if not Q:
		#	return new
		for q in Q:
			n=[]
			for s in S:
				if q == s:
					n.append(str(1))
				else:
					n.append(str(0))
			new.append(n)

		blah=[]
		#for s in S:
		#	blah.append(s.strip())
		#print "\t".join(blah)
		#for row in new:
		#	print "\t".join(row)
			#print row
		return new

	def runTable(self,table,i=0):
		i=0
		for row in table:
			next=table[i+1]
	
			b=0
			for col in row:
				b+=1

			i+=1


			




	def parse(self,filename):
		result=[]
		data=file(filename,'r').readlines()
		print len(data)
		N=int(data[0].strip())
		n=1
		i=1
		while n <= N:
			s=int(data[i])
			i+=1
			S=data[i:i+s]
			i+=s
			q=int(data[i])
			i+=1
			Q=data[i:i+q]
			#print 'run'
			#print "count: %s %s " % (len(S),len(Q))
			if 1:#n == 7:
				#print 'n %s' % n
				self.dataLength=q
				print len(Q)
				table=self.makeTable(S,Q)
				self.shortSwitch=99999
				#self.findSegs(table,S)
				#print self.shortSwitch
				#raw_input()
				self.lookup={}
				#print "###############"
				if len(Q) >= 300:
					pass
				else:#if n == 9:
					print len(Q)
					self.cache=0
					self.nocache=0
					self.almostcache=0
					self.ugh={}
					self.dup=0
					self.least=99999
					print "LEN %s" % self.dataLength
					total=self.recurse(Q,i=0,switches=99999,count=0,searchengines=S,start=True,lookup=True)
					l1=self.least
					print "T C N A D: %s %s %s %s %s" % (total,self.cache,self.nocache,self.almostcache,self.dup)
				#	print self.lookup
					#total=0
					#######
					#self.least=99999
					#total2=self.recurse(Q,i=0,switches=99999,count=0,searchengines=S,start=True)
					#l2=self.least
					#print "DONE"
					#print total2
					##print "DONE"
					#print "T1 T2 L1 L2: %s %s %s %s" % (total,total2,l1,l2)
				#total=self.findLeast(S,Q)#(Q,i=0,switches=99999,count=0,searchengines=S)
				#print 't2 %s' % total2
				#if total > 1:
				#	total-=1
				#print 't %s' % total
				#print "s=%s" % s
				#print "q=%s" % q
				#print "S=%s" % S
				#print "Q=%s" % Q
				#print "n=%s" % n
				result.append("Case #%s: %s" % (n,total))
			n+=1
			i+=q
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
	#for key,item in a.queryData.items():
	#	print "final %s %s" % (key,a.recurse(a.queryData[key]))
#	print a.queryData
#	print len(a.queryData[1])
#	print a.searchEngines

