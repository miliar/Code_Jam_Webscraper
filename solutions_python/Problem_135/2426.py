#!/usr/bin/env python
import sys

	
class TestCase:
	def __init__(self, data):
		answerA = int(data[0])
		answerB = int(data[5])
		arrangementA = [i.strip().split(" ") for i in data[1:5]]
		arrangementB = [i.strip().split(" ") for i in data[6:10]]
		possibleA = arrangementA[answerA-1]
		possibleB = arrangementB[answerB-1]
		self.overlap = list(set(possibleA) & set(possibleB))
		
	def outcome(self):
		if len(self.overlap) == 0:
			return "Volunteer cheated!"
		elif len(self.overlap) == 1:
			return self.overlap[0]
		else:
			return "Bad magician!"




if __name__ == "__main__":
	with open(sys.argv[1]) as df:
		data = df.readlines()

	T = int(data[0])
	
	rf = open("res.txt", "w")
	for t in range(T):
		l_bound = t * 10 + 1
		u_bound = t * 10 + 11
		dataset = data[l_bound:u_bound]
		case = TestCase(dataset)
		outcome = case.outcome()
		rf.write("Case #%s: " % (t+1))
		rf.write("%s" % outcome)
		if t != T-1:
			rf.write("\n")
	
	rf.close()
