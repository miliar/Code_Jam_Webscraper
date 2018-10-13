import sys

def main():
	count = int(sys.stdin.readline())
	for i in range(count):
		countA, countB = Timetable().process()
		print "Case #%d: %d %d" % (i + 1, countA, countB)

STATIONA = 0
STATIONB = 1

class Timetable:
	def __init__(self):
		pass
	def process(self):
		# read T
		turnaround = int(sys.stdin.readline())
		self.queues = (Queue(turnaround), Queue(turnaround))
		# read NA,NB
		counts = sys.stdin.readline().split()
		countAB = int(counts[0])
		countBA = int(counts[1])
		self.readStation(countAB, STATIONA, STATIONB)
		self.readStation(countBA, STATIONB, STATIONA)
		# calculate required trains
		countA = self.queues[STATIONA].calcRequiredTrains()
		countB = self.queues[STATIONB].calcRequiredTrains()
		return (countA, countB)
	def readStation(self, count, origin, destination):
		for i in range(count):
			self.readTrain(origin, destination)
	def readTrain(self, origin, destination):
		times = sys.stdin.readline().split()
		self.queues[origin].addDeparture(self.parseTime(times[0]))
		self.queues[destination].addArrival(self.parseTime(times[1]))
	def parseTime(self, time):
		return 100 * int(time[0:2]) + int(time[3:5])

ARRIVE = 0
DEPART = 1

class Queue:
	def __init__(self, turnaround):
		self.times = []
		self.turnaround = turnaround
	def addDeparture(self, time):
		self.add(DEPART, time)
	def addArrival(self, time):
		self.add(ARRIVE, time + self.turnaround)
	def add(self, type, time):
		self.times.append((time, type))
	def calcRequiredTrains(self):
		self.times.sort()
		needed = 0
		available = 0
		for time, type in self.times:
			if type == ARRIVE:
				#print "Train arrives %s" % time
				available += 1
			else:
				if available == 0:
					#print "New",
					needed += 1
				else:
					available -= 1
				#print "Train leaves %s" % time
		return needed

if __name__ == "__main__":
    sys.exit(main())
