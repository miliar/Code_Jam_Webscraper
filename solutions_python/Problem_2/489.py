
def convert(timeStr):
	print timeStr
	times = timeStr.split(' ')
	parts =[]
	for item in times:
		res= item.split(':')
		parts.extend(res)
	print parts
	return ((int(parts[0]), int(parts[1])), (int(parts[2]), int(parts[3])))

def add_times(start, adder):
	print start
	print adder
	if adder[1]+start[1] > 60:
		return (start[0]+1, (start[1]+adder[1])-60)
	return (start[0]+adder[0], start[1]+adder[1])
	
def time_cmp(x, y):
	return cmp(x.time, y.time)



class Station:
	def __init__(self, schedule, turnaround):
		self.sched = schedule
		self.sched.sort()
		self.t = turnaround
		self.trains = []
		self.new = 0
		self.other=None
		
	def sendOff(self, time):
		if len(self.trains)>0:
			for train in self.trains:
				print "sendOff", self
				print train.ready(self.t)
				print time[0]
				if cmp(train.ready(self.t), time[0]) <=0:
					self.trains.remove(train)
					train.time=time
					self.other.recieve(train)
					break
			#python treats this as a "finally" clause, which is not triggered on abreak. :D Thanks Bryan!
			else:
				print "otherwise"
				self.new +=1
				self.other.recieve(Train(time))
		else:
			print "no trains"
			self.new+=1
			self.other.recieve(Train(time))
			
	def recieve(self, train):
		self.trains.append(train)
		print self.trains
		self.trains.sort(cmp=time_cmp)
		print self.trains
		
	def run(self):
		#creates a generator function, saves me from writing multi-threaded code
		if len(self.sched)>0:
			
			latest = self.sched[0]
			print "run", latest
			self.sched = self.sched[1:]
			print self.sched
			self.sendOff(latest)
			return 1
		else:
			return -1
			
	
		
class Train:
	def __init__(self, time):
		self.time=time
		
	def ready(self, t):
		return add_times(self.time[1], t)
		
	def __repr__(self):
		return "Train:"+str(self.time)
		
def main(schedA, schedB, turnaround):
	stationA=Station(schedA, turnaround)
	stationB=Station(schedB, turnaround)
	stationA.other=stationB
	stationB.other=stationA
	masterSched = {}
	keys = set(schedA)
	keys.update(set(schedB))
	keys=list(keys)
	keys.sort()
	print keys
	for key in keys:
		masterSched[key]=[station for station in [stationA, stationB] if station.sched.count(key) >=1]
	for key in keys:
		print "key:",
		print key
		for item in masterSched[key]:
			print "item",item
			print "item.new",item.new
			print "item.trains",item.trains
			item.run()
	return stationA.new, stationB.new
	
def readFile(fname):
	f=open(fname, 'r')
	r=open(fname+'results', 'w')
	lines = f.readlines()
	n=int(lines[0])
	index=1
	for i in range(1, n+1):
		print index
		t=int(lines[index])
		t=(0, t)
		schedAB = lines[index+1]
		a, b = schedAB.split(' ')
		a=int(a)
		b=int(b)
		print a, b
		schedA = []
		schedB = []
		for j in range(a):
			schedA.append(convert(lines[index+2+j]))
		index+=a
		for k in range(b):
			schedB.append(convert(lines[index+2+k]))
		print schedA, schedB
		na, nb = main(schedA, schedB, t)
		print na, nb
		if na+nb <= a+b:
			r.write("Case #%d: %d %d\n" % (i,na, nb))
		else:
			print "ERROR!"
			print i, schedA, schedB
			f.close()
			r.close()
			return
		index+=b+2
	f.close()
	r.close()