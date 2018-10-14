import sys
import heapq

def main():
	with open("A-small-attempt1.in", "r+") as f:
		lines = f.readlines()[1:]
		f2 = open("output","a+")
		num = 1
		for l in lines:
			s = Solver(l.split(" ")[0],int(l.split(" ")[1]))
			k = s.solve()
			row = "Case #"+str(num)+": "+str(k)+"\n"
			num=num+1
			f2.write(row)
	


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

		

class Solver(object):
	"""docstring for Solver"""
	def __init__(self, pancakes, flipperSize):
		super(Solver, self).__init__()
		self.pancakes = list(pancakes)
		self.flipperSize = flipperSize


	def union(self, produced):
		unioned = []
		for i in produced:
			if i != produced[-1]:
				unioned.append(i[0])
			else:
				unioned += i

		return unioned

	def calculateDistance(self,l):
		dist = len(l) - l.count(False)

		return dist

	def flip(self, lToFlip):
		new = []
		for i in lToFlip:
			if i == "+":
				new.append("-")
			else:
				new.append("+")
		return new

	def solve(self):
		frontier = PriorityQueue()
		frontier.put(self.pancakes, 0)
		came_from = {}
		cost_so_far = {}
		came_from[''.join(self.pancakes)] = None
		cost_so_far[''.join(self.pancakes)] = 0

		while not frontier.empty():
			current = frontier.get()
		    
			if current == ['+']*len(current):
				break
			for next in self.neighbors(current):
				new_cost = cost_so_far[''.join(current)] + 1
				if ''.join(next) not in cost_so_far or new_cost < cost_so_far[''.join(next)]:
					cost_so_far[''.join(next)] = new_cost
					priority = new_cost + self.calculateDistance(next)
					frontier.put(next, priority)
					came_from[''.join(next)] = current

		
		try:
			return cost_so_far['+'*len(self.pancakes)]
		except:
			return "IMPOSSIBLE" 

	def neighbors(self, current):
		ns = []
		for i in range(len(current)-self.flipperSize+1):
			ns.append(current[:i] + self.flip(current[i:i+self.flipperSize]) + current[i+self.flipperSize:])
		return ns



		

if __name__ == '__main__':
	main()