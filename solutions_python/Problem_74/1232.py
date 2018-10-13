#!/usr/bin/python
import sys
import string

def alg(case,f): 
	row = f.readline().split()
	moves = int(row[0])
	pO = pB = 1
	tO = tB = 0
	for i in range(moves):
		who = row[i*2+1]
		btn = int(row[i*2+2])
		
		if (who == 'O'):
			tO += abs(btn-pO) # go
			if (tB>=tO): tO=tB # wait before press
			tO+=1 # and press 
			pO=btn
		else: # who == 'B'
			tB += abs(btn-pB) # go
			if (tO>=tB): tB=tO # wait before press
			tB+=1 # and press 
			pB=btn
	
	print 'Case #%d: %d'%(case+1,max(tO,tB)) 

def main(argv):
	with open(argv[1],'r') as f:
		cases =	int(f.readline())
		for i in range(cases):
			alg(i,f)
	f.closed

if __name__ == "__main__":
	main(sys.argv)	
