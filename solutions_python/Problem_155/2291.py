class Problem:
	def __init__(self, desc):
		self.people = [int(x) for x in desc.split(" ")[1]]

	def solve(self):
		print "Solving..."
		i = 0
		standing = 0
		needed = 0
		while i < len(self.people):
			if standing < i:
				friends = i - standing
				needed += friends
				standing += friends
			standing += self.people[i]
			i += 1
		return needed


with open("input.txt") as f:
	f.readline()
	problems = f.readlines()
	answers = [Problem(p.strip()).solve() for p in problems]
	finals = ["Case #%d: %s" % (i + 1, a) for i, a in enumerate(answers)]
	with open("output.txt", 'w') as fout:
		fout.write("\n".join(finals))