#!/usr/bin/python
from string import atoi
from sys import argv 
import math

def solve(inputfile):
	f = open(inputfile, "r")
	cases = atoi(f.readline())	

	for case in range(cases):
		print "Case #%d:"%(case+1)
		score = []
		for tnum in range(1, atoi(f.readline())+1):
			t = f.readline()	
			score.append(t)	
			
		wp = []
		for t in score:
			win = 0.0
			lose = 0.0
			for c in t:
				if c == '1': win += 1
				elif c == '0': lose+= 1
			wp.append(win/(win+lose))
			
		owp = []
		xnum = 0
		for x in score:
			tnum = 0
			tg = 0 
			owptally = 0
			for t in x:
				win = 0.0
				lose = 0.0
				cnum = 0
				if t == '1' or t == '0':
					tg += 1
					for c in score[tnum]:
						if cnum != xnum:	
							if c == '1': win += 1
							elif c == '0': lose+= 1
						cnum += 1
					#print owptally
					owptally += win/(win+lose)
				tnum += 1
			owp.append(owptally/(tg))
			xnum += 1

		oowp = [] 
		xnum = 0
		for x in score:
			tnum = 0
			oowptally = 0
			cnum =0 
			for t in x:
				if t == '1' or t == '0':
					oowptally += owp[tnum]
					cnum += 1
				tnum+=1
			xnum += 1
			
			oowp.append(oowptally/cnum)

		rpis = oowp
		for x in range(len(score)):
			#print "wp:", wp[x],"owp", owp[x],"oowp", oowp[x]
			rpi = .25*wp[x] + .5*owp[x]+ .25*oowp[x]
			print rpi


if __name__ == "__main__": solve(argv[1])
