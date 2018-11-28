import sys

def fill_to_capacity(groups,returners,capacity):
	count,cur_capacity = 0,0
	while cur_capacity < capacity:
		if len(groups) == 0:
			break
		people = groups[0]
		if cur_capacity + people <= capacity:
			people = groups.pop(0)
			cur_capacity += people
			count += people
			returners.append(people)
		else:
			break #stop adding people
	return count

class DayRun:
	def __init__(self,runs,capacity,N,groups):
		self.groups = []
		for x in groups[:N]:
			self.groups.append(x)
		self.runs = runs
		self.capacity = capacity

	def simulate(self):
		count = 0
		cur_capacity = 0
		rem = list(self.groups)
		returners = []
		for run in range(self.runs):
			count += fill_to_capacity(rem,returners,self.capacity)
			rem += returners
			returners = []
		return count

def handle_input(filename):
	afile = open(filename)
	cases = int(afile.readline())
	for case in xrange(cases):
		R,k,N = map(int,afile.readline().split())
		groups = map(int,afile.readline().split())
		euros = DayRun(R,k,N,groups).simulate()
		print "Case #"+str(case+1)+": "+str(euros)

if __name__ == "__main__":
	handle_input(sys.argv[1])
