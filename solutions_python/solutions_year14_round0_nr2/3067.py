#!/usr/bin/python
import sys
import os

test_cases = 0

#base CPS is 2 according to the problem
class ccGame(object):
	
	def __init__(self, farmCost, farmCPS, cookiesToWin):
		self.farmCost = float(farmCost)
		self.farmCPS = float(farmCPS)
		self.cookiesToWin = float(cookiesToWin)
		self.farms = 0
		
	def timeToFarm(self):
		return self.farmCost/(2 + self.farms*self.farmCPS)
	
	def timeToWin(self):
		return self.cookiesToWin/(2 + self.farms*self.farmCPS)
	
	def timeToWinWithAnotherFarm(self):
		return (self.cookiesToWin)/(2 + ((self.farms + 1) * self.farmCPS)) + self.timeToFarm()
		
	def simulate(self):
		wait = False
		time = 0.0
		self.farms = 0
		while (wait == False):
			t_wf = self.timeToWinWithAnotherFarm()
			t_w = self.timeToWin()
			t_f = self.timeToFarm()
			cps = 2 + self.farms*self.farmCPS
			#print "summary: cps=" + str(cps) + ", time=" + str(time) + ", t_wf=" + str(t_wf) + ", t_w=" + str(t_w) + ", t_f=" + str(t_f) + ", farms=" + str(self.farms)
			if(t_wf < t_w):
				#buy farm
				time = time + self.timeToFarm()
				self.farms = self.farms + 1	
			else:
				#wait
				time = time + self.timeToWin()
				wait = True
		return "{:.7f}".format(time) # 7 decimal places was specified by google


def get_input():
	if(len(sys.argv) < 2):
		print "No filename specified.\nUsage: python " + sys.argv[0] + " filename"
	filename = sys.argv[1]
	if(os.path.isfile(filename)):
		return open(sys.argv[1], 'r')
	else:
		print "file " + filename + " not found."
	exit()
		
		
def parse_input(input):
	global test_cases
	test_cases = int(input.readline())
	ccGames = []
	for x in range(0, test_cases):
		game_parameters = input.readline().split()
		farmCost = game_parameters[0]
		farmCPS = game_parameters[1]
		cookiesToWin = game_parameters[2]
		ccGames.append(ccGame(farmCost, farmCPS, cookiesToWin))
	return ccGames
	
input = get_input()
ccGames = parse_input(input)
output_filename = sys.argv[1] + ".out"
output = open(output_filename, 'w')
for x in range(0, len(ccGames)):
		output.write("Case #" + str(x + 1) + ": " + ccGames[x].simulate() + "\n")
#solve and write to the file
output.close()