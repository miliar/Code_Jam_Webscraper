#################
# Google CodeJam 2011
# Qualification Round: Problem A - "Bot Trust"
# Britt Gresham - (demophoon7575@gmail.com)
#################

import sys
import re

class bot:
	def __init__(this,name,move):
		this.button = 1
		this.step = 0
		this.name = name
		this.moves = move
		
	def nextMove(this,f):
		if not(this.currentMove() == None):
			if this.button == int(this.currentMove()[1]) and f:
				this.step += 1
				# print this.name + " -  step:   " + str(this.step) + str(this.currentMove())
				# print this.name + " Pushed " + str(this.button)
				return True
			else:
				if this.button > int(this.currentMove()[1]):
					this.button += -1
					# print this.name + " Move 2 " + str(this.button)
				elif this.button < int(this.currentMove()[1]):
					this.button += 1
					# print this.name + " Move 2 " + str(this.button)
			return False
				
	def currentMove(this):
		if this.moves:
			if (this.step) < len(this.moves):
				return this.moves[this.step]
			else:
				return None
		else:
			return None

class game:
	def __init__(this,trial,case):
		this.move = 1
		this.step = 0
		this.case = case
		this.directions = trial
		this.p1 = bot("Orange",[i for i in trial if re.search(r"O",i[0])])
		this.p2 = bot("Blue  ",[i for i in trial if re.search(r"B",i[0])])
	
	def play(this):
		
		x = 0
		while not(this.p1.currentMove() == None) or not(this.p2.currentMove() == None):
			# print "\n" + str(this.move)
			if this.directions[x] == this.p1.currentMove():
				if this.p1.nextMove(True):
					this.p2.nextMove(False)
					x += 1
				else:
					this.p2.nextMove(False)
			else:
				if this.p2.nextMove(True):
					this.p1.nextMove(False)
					x += 1
				else:
					this.p1.nextMove(False)
			this.move += 1
		
				
	
	def results(this):
		return "Case #" + str(this.case) + ": " + str(this.move - 1)
		
def main():
	# Command line arguments
	args = sys.argv[1:]
	if not(args):
		print "Usage: qualA.py infilename outfilename"
		exit(1)
	
	file = open(args[0],"r")
	trials = []
	case = 1
	
	for line in file:
		trials.append(re.findall(r"([OB])\s(\d+)",line))
	file.close()
	
	caseMax = len(trials)
	trials = trials[1:]
	
	output = ""
	
	for x in range(case - 1,caseMax - 1):
		# Initialize Game
		trial = game(trials[x],(x + 1))
		trial.play()
		output += trial.results() + "\n"
		
	print output
	
	file = open(args[1],"w")
	file.write(output)

if __name__ == "__main__":
	main()