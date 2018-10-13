import math
#import copy
from datetime import datetime

import psyco
psyco.full()

def printMsg(msg):
	if (True):
		print msg
		
##############################################

class Solver:
	labels = "abcdefghijklmnopqrstuvwxyz"
#	labels = "ab"
	
	def __init__(self):
		None

	def reset(self):
		None

	def answer(self, map, h, w):
		ans = []
		
		flowdir = []
		sink = {}
		for y in range(0, h):
			row = []
			ansrow = []
			up = y == 0
			bottom = y== h-1
			for x in range(0, w):
				ansrow += ['?', ]
				left = x == 0
				right = x == w - 1
				if up:
					nc = 10000
				else :
					nc = map[y-1][x]
				if bottom:
					sc = 10000
				else :
					sc = map[y+1][x]
				if left:
					wc = 10000
				else :
					wc = map[y][x-1]
				if right:
					ec = 10000
				else :
					ec = map[y][x+1]
				
				#print map[y][x], nc, wc, ec, sc, '|', 
				dir = 0
				if (map[y][x] > nc and nc <= wc and nc <= ec and nc <= sc):
					dir = 1
				elif (map[y][x] > wc and wc <= ec and wc <= sc):
					dir = 2
				elif (map[y][x] > ec and ec <= sc):
					dir = 3
				elif (map[y][x] > sc):
					dir = 4
				else:
					sink[(x, y)] = []
	         				
				print dir, 
				row += [dir, ]
			print
			flowdir += [row, ]
			ans += [ansrow, ]
		#print flowdir
		#print ans
		
		groups = {}
		for y in range(0, h):
			for x in range(0, w):
				if not groups.has_key((x, y)):
					dir = flowdir[y][x]
					if (dir == 0):
						groups[(x, y)] = (x, y)
					else:
						unknownSet = [(x, y)]
						found = False
						tx = x
						ty = y
						sinkxy = None
						while not found:				
							(ny, nx) = self.next(flowdir[ty][tx], tx, ty)
							if groups.has_key((nx, ny)):
								found = True
								sinkxy = groups[(nx, ny)]
							else:
								unknownSet += [(nx, ny)]
								if flowdir[ny][nx] == 0:
									found = True
									sinkxy = (nx, ny)
								else:
									tx = nx
									ty = ny
						for c in unknownSet:
							groups[c] = sinkxy
							
		curLabel = 0
		ans[0][0] = self.labels[curLabel]
		
		sinkLabel = {}
		sinkLabel[groups[(0, 0)]] = self.labels[curLabel]
		for y in range(0, h):
			for x in range(0, w):
				if sinkLabel.has_key(groups[(x, y)]):
					ans[y][x] = sinkLabel[groups[(x, y)]]
				else :
					curLabel += 1
					sinkLabel[groups[(x, y)]] = self.labels[curLabel]
					ans[y][x] = self.labels[curLabel]
					
#		groups = {}
#		for y in range(0, h):
#			for x in range(0, w):
#				dir = flowdir[y][x]
#				if (dir == 0):
#					groups[(x, y)] = [(x, y)]
#				else:
#					(ny, nx) = self.next(dir, x, y)
#					if groups.has_key((nx, ny)):
#						temp = groups[(nx, ny)][:]
#						groups[(x, y)] = temp+[(x, y)]
#						groups.pop((nx, ny))
#					else:
#						found = False
#						for key, g in groups.items():
#							if (ny, nx) in g:
#								g += [(x, y)]
#								groups[key] = g
#								found = True
#						if not found:
#							groups[(x, y)] = [(x, y), (nx, ny)]
#
#		print h, w, len(groups),  groups
#		if len(groups) > 2:
#			exit()
#		curLabel = 0
#		ans[0][0] = self.labels[curLabel]
#		for y in range(0, h):
#			up = y == 0
#			bottom = y== h-1
#			for x in range(0, w):
#				left = x == 0
#				right = x == w - 1
#				
#				dir = flowdir[y][x]
#				(ny, nx) = self.next(dir, x, y)
#
#				if ans[y][x] == "?":
#					if dir == 0:
#						curLabel += 1
#						ans[y][x] = self.labels[curLabel]
#					else:
#						if ans[ny][nx] == "?":
#							unknowSet = [(nx, ny)]
#							found = False
#							tx = nx
#							ty = ny
#							while not found:
#								(ty, tx) = self.next(flowdir[ty][tx], tx, ty)
#								if ans[ty][tx] == "?":
#									if flowdir[ty][tx] == 0:
#										curLabel += 1
#										label = self.labels[curLabel]
#										found = True
#									else:
#										unknowSet += [(tx, ty), ]
#										(ty, tx) = self.next(flowdir[ty][tx], tx, ty)
#								else:
#									label = ans[ty][tx]
#									found = True
#							
#							for cell in unknowSet:
#								ans[cell[1]][cell[0]] = label
#							ans[y][x] = label
##							if flowdir[ny][nx] == 0 or flowdir[ny][nx] > 2:
##								curLabel += 1
##								ans[y][x] = self.labels[curLabel]
##								ans[ny][nx] = ans[y][x]
##							else:
##								ans[y][x] = self.labels[curLabel]
#						else : 
#							ans[y][x] = ans[ny][nx]
#				else:
#					if dir > 0:
#						if ans[ny][nx] == "?":
#							ans[ny][nx] = ans[y][x]
						
		return ans

	def next(self, dir, x, y):
		ny = y
		nx = x
		if dir > 0:
			if dir == 1:
				ny = y - 1
				nx = x
			elif dir == 2:
				ny = y
				nx = x - 1
			elif dir == 3:
				ny = y
				nx = x + 1
			elif dir == 4:
				ny = y + 1
				nx = x
		return ny, nx
		
##############################################

prjId = "qr_b"

_MIN_CASES = 999
testCase = "large"
#testCase = "small"

#infilename="./data/A-"+testCase+"-practice.in"
#infilename="./data/A-small-attempt0.in"
#infilename="./data/sample.in"
infilename="./data/B-large.in"
outfile = "./out/"+prjId+"_"+ testCase +"_ans.out"

inf = open(infilename, "r")
outf = open(outfile, "w")

numCases = int(inf.readline())

solver = Solver()
stTime = datetime.now()

print "Start", stTime
for i in range(1, min(numCases+1, _MIN_CASES +1)):
	line = inf.readline().strip()
	token = line.split()
	h = int(token[0])
	w = int(token[1])
	map = []
	for j in range(0, h):
		line = inf.readline().strip()
		token = line.split()
		row = []
		for cell in token:
			row += [int(cell), ]
		map += [row, ]
	#print map
	solver.reset()
	ans = solver.answer(map, h, w)
	print "Case #%d:" % i
#	outf.write("Case #%d: %s" % (i, ans))
#	outf.write("\n")
	outf.write("Case #%d:\n" % i)
	for l in ans:
		outline = ' '.join(l)
		outf.write("%s\n" % outline)
		print outline
	#break

endTime = datetime.now()
print "End",  endTime
print endTime - stTime

inf.close()
outf.close()
