import sys
from gcjparser import Parser
from time import time

def parse(filename):
	fin = file(filename, 'r')
	numCases = int( fin.readline().strip() )

	for caseData in range(numCases):
		numPoints, dist = fin.readline().strip().split(' ')

		pointStats = []
 		for i in range(int(numPoints)):
			point, count = fin.readline().strip().split(' ')
			pointStats.append([int(point), int(count)*int(dist)])
		yield Case(pointStats, int(dist))

class Point(object):
	def __init__(this, center, weight):
		this.center = center
		this.weight = weight

class Group(object):
	def __init__(this, points):
		this.points = points
		this.center = (max(p.center for p in points) + min(p.center for p in points)) /2.
		this.weight = sum(p.weight for p in points)

	def makeGroup(this, otherGroup):
		return Group(this.points + otherGroup.points)

	def intersects(this, otherGroup):
		return abs(this.center - otherGroup.center)*2 < (this.weight + otherGroup.weight)

	def getAnswer(this):
		answer = 0
		points = sorted(this.points, key=lambda p:p.center)
		left = this.center - this.weight/(2.)
		for p in points:
			curAnswer = max(abs(p.center-left), abs(p.center-left-p.weight))
			answer = max(answer, curAnswer)
			left += p.weight
		return answer

	def __repr__(this):
		return "Group(%.2f, %.2f) [%.1f] {%.1f}"%(this.center - this.weight/2., this.center + this.weight/2., this.getAnswer(), this.center)

class Case(object):
	def __init__(this, pointStats, dist):
		this.pointStats = pointStats
		this.dist = dist
		this.points = [Point(center, weight) for center, weight in pointStats]
		this.groups = [Group([p]) for p in this.points]
		for g in this.groups:
			print g,
		print ""

	def findGroupIntersects(this):
		groups = this.groups
		numGroups = len(groups)
		for i in range(numGroups-1):
			if groups[i].intersects(groups[i+1]):
				this.joinGroupWithNext(i)
				return True
		return False

	def joinGroupWithNext(this, idx):
		group1 = this.groups[idx]
		group2 = this.groups[idx+1]
		this.groups[idx] = group1.makeGroup(group2)
		del this.groups[idx+1]

	def solve(this):
		while this.findGroupIntersects():
			print ".",
		this.answer = max(g.getAnswer() for g in this.groups);
		this.answer -= this.dist/2.;

	def pprint(this, caseNum, fout):
		"""if this.answer == int(this.answer):
			fout.write("Case #%d: %d\n"%(caseNum, int(this.answer)))
		else:"""
		fout.write("Case #%d: %s\n"%(caseNum, this.answer))

def main(filein, fileout):
	start = time()

	fout = file(fileout, 'w')
	cases = parse(filein)

	for i, x in enumerate(cases):
		print "Case %d: "%(i+1),
		x.solve()
		print ". Done!"
		print x.groups
		x.pprint(i+1, fout)

	end = time()
	print "Total time=%s"%(end-start)

if __name__ == '__main__':
    main("B-small-attempt2.in", "output.txt")
	#print calcPointsLeft('abcd', 'epnzavjbrdohskcliqygfumxwt', 'd')
