#!/usr/bin/python
import sys

def main():
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[1][:-2] + 'out', 'w')
	
	for case in xrange(1, int(infile.readline())+1):
		chickcount, minchicks, barloc, endtime = (int(number) for number in infile.readline().split())
		chicklocs = [int(loc) for loc in infile.readline().split()]
		chickspeeds = [int(speed) for speed in infile.readline().split()]
		chicks = []
		annoyingchicks = []
		# seperate chicks that can actually make it from those that can't
		for i in xrange(chickcount):
			if (chicklocs[i]+(chickspeeds[i]*endtime))>=barloc:
				chicks.append(chicklocs[i])
			else:
				annoyingchicks.append(chicklocs[i])
		
		# can we meet our quota?
		if len(chicks)<minchicks:
			outfile.write("Case #%i: IMPOSSIBLE\n"%(case,))
			continue
		elif minchicks==0:
			outfile.write("Case #%i: 0\n"%(case,))
			continue
		
		# remove unneeded chicks
		while len(chicks)>minchicks:
			lowest = 0
			for i in xrange(1, len(chicks)):
				if chicks[i]<chicks[lowest]:
					lowest = i
			chicks.pop(lowest)
		
		lowestvalue = chicks[0]
		for i in xrange(1, len(chicks)):
			if chicks[i]<lowestvalue:
				lowest = i
				lowestvalue = chicks[i]

		actions = 0
		for bad_chick in annoyingchicks:
			if bad_chick>=lowestvalue:
				for chick in chicks:
					if chick<bad_chick: actions+=1
		
		outfile.write("Case #%i: %i\n"%(case, actions))


if __name__ == "__main__":
	main()
