from threading import *
import sys
import copy
import time

done = []

class Solver():

	def __init__(self, caseId, inArray, array, answer):
		self.caseId = caseId
		self.target = array
		self.answer = answer
		self.base = inArray

	def maxLines(self, line):
		maxL = 0
		for i in line:
			if i > maxL:
				maxL = i
		return maxL

	def nonMaxLines(self, lines, maxL):
		res = []
		for i in range(len(lines)):
			if lines[i] < maxL:
				res.append(i)
		return res

	def processLine(self, target):
		r = 0
		for i in range(len(target)):
			if target[i] > r:
				r = target[i]
		return r

	def processCol(self, target, col):
		r = 0
		for i in range(len(target)):
			if target[i][col] > r:
				r = target[i][col]
		return r
		
	def canProcessCall(self, val, col, base, target):
		for i in range(len(base)):
			if target[i][col] > val:
				return False

		return True

	def run(self, base, target):

		n = len(target)
                m = len(target[0])

		for i in range(n):
			r = self.processLine(target[i])
			for j in range(m):
				if base[i][j] > r:
					base[i][j] = r

		for j in range(m):
			r = self.processCol(target, j)
			for i in range(n):
				if base[i][j] > r:
					base[i][j] = r

		
		if self.finalArray(base):
			self.answer[self.caseId] = "Case #" + str(self.caseId) + ": YES"
		else:
			self.answer[self.caseId] = "Case #" + str(self.caseId) + ": NO"

	def finalArray(self, tmp):
		n = len(self.target)
		m = len(self.target[0])
		for i in range(n):
			for j in range(m):
				if self.target[i][j] != tmp[i][j]:
					return False
		return True
		
def maxVFunction(base):
	maxV = 0
	for i in base:
		for j in i:
			if j > maxV:
				maxV = j
	return maxV
	

def prepare():
	lines = sys.stdin.readlines()
	nbCase = int(lines[0])
	case = {}
	baseLine = 1
	for i in range(nbCase):
		split = lines[baseLine].split(' ')
	        n = int(split[0])
        	m = int(split[1])
		case[i] = []
		for j in range(n):
			case[i].append([])
			split2 = lines[baseLine+1+j].split(' ')
			for k in range(len(split2)):
				case[i][j].append(int(split2[k]))
		baseLine += n + 1
	return case

if __name__ == "__main__":

	prep = prepare()
	answer = {}
	for i in prep:
		inArray = []
		for j in range(len(prep[i])):
			inArray.append([])
			l = len(prep[i][j])
			for k in range(l):
				inArray[j].append(100)
		answer[i+1] = "Case #" + str(i+1) + ": NO"
		Solver(i+1, inArray, prep[i], answer).run(inArray, prep[i])
		print answer[i+1]
