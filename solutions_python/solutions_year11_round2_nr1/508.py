#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import sys

class gcj:
    IN = sys.stdin
    number = 0

    @classmethod
    def case(cls):
        cls.number += 1
        return 'Case #%d:' % cls.number

    @classmethod
    def line(cls, type=str):
        line = cls.IN.readline()
        return type(line.strip('\n'))

    @classmethod
    def splitline(cls, type=str):
        line = cls.IN.readline()
        return [type(x) for x in line.split()]

def calWp(t):
	"""docstring for calWp"""
	n = len(t)
	score = 0
	num = 0
	for i in xrange(n):
		if t[i] != '.':
			if t[i] == '1':
				score += 1
				num += 1
			else:
				num += 1
	return float(score)/num


def removeOppoentScore(op, selfScores):
	"""docstring for removeOppoentScore"""
	n = len(selfScores)
	tmp = []
	for i in xrange(n):
		if i != op:
			tmp.append(selfScores[i])
	return tmp

def calOwp(s, b):
	"""docstring for calOwp"""
	op_score_wt_me = 0
	me = 0
	counter = 0
	subCounter = 0
	n = len(s)
	owpScore = []
	for s in b:
		owpLst = []
		for i in xrange(n):
			if i != me:
				if s[i] != '.':
					# print me, b[i]
					owpLst.append(calWp(removeOppoentScore(me, b[i])))
		
		me += 1
		if len(owpLst) > 0:
			tmp = sum(owpLst) / len(owpLst)
		else:
			tmp = 0.0
		owpScore.append(tmp)
	
	# print owpScore
	return owpScore
	
def calOOwp(owpScores, b):
	n = len(b)
	oowpScore = []
	for s in b:
		oowpLst = []
		for i in xrange(n):
			if s[i] != '.':
				oowpLst.append(owpScores[i])
		
		if len(oowpLst) > 0:
			oowpS = float(sum(oowpLst)) / len(oowpLst)
		else:
			oowpS = 0.0
		oowpScore.append(oowpS)
	
	# print oowpScore
	return oowpScore
	
def solve(f):
	N = int(f.readline())
	RPI = []
	board = [gcj.line() for _ in xrange(N)]
	# print board
	scores = []
	for team in board:
		wp = calWp(team)
		scores.append(wp)
	
	owpScores = calOwp(scores, board)
	oowpScores = calOOwp(owpScores, board)
	n = len(owpScores)
	for i in xrange(n):
		temp = 0.25 * scores[i] + 0.50 * owpScores[i] + 0.25 * oowpScores[i]
		RPI.append(temp)
	# print RPI
	return  RPI



f = sys.stdin
n = int(f.readline())

for i in xrange(n):
	res = solve(f)
	print "Case #%d:" % (i+1)
	for x in res:
		print "%.12f" %x