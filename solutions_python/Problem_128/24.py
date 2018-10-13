from math import *;
#INPUT_NAME = 'C-large.in'
#OUTPUT_NAME = 'C-large.out'
INPUT_NAME = 'C-small-attempt0.in'
OUTPUT_NAME = 'C-small_0.out'
#INPUT_NAME = 'C.in'
#OUTPUT_NAME = 'C.out'
		
def solve(T):
	# go through the tribes logging attack days & regions, sorted by time
	events = []
	minD = 0
	maxD = 0	
	for i in T:
		(d, n, w, e, s, dd, dp, ds) = i
		(curd, curw, cure, curs) = (d,w,e,s)		
		for i in xrange(n):
			events.append((curd, curs, curw, cure))
			curd += dd
			curw += dp
			cure += dp
			curs += ds
			if curw < minD:
				minD = curw
			if cure > maxD:
				maxD = cure
				
	events.sort()	
	wall = [0 for i in xrange(2*(maxD-minD+1))]
	pwall = [0 for i in xrange(2*(maxD-minD+1))]
	
	#simulate wall growth
	nsuccessful = 0
	prevday = -1
	toUpdate = []
	for ev in events:
		(d, s, w, e) = ev
		if(prevday!=d):
			for pos in toUpdate:
				pwall[pos] = wall[pos]
			toUpdate = []
			prevday = d
				
		succ = False
		for j in xrange(2*(w-minD), 2*(e-minD)+1):
			if(pwall[j]<s):
				succ = True
				toUpdate.append(j)
				wall[j] = s
		
		if succ:
			nsuccessful += 1
		
	return nsuccessful
	
	
	
	
# THIS IS THE "MAIN" FUNCTION
def fullsol(slst):	
	T = int(slst[0]) # number of test cases
	cur = 1
	sol = []
	for i in xrange(T):
		N = int(slst[cur])
		cur += 1
		tribes = []
		for j in xrange(N):
			tribes.append(map(int, slst[cur].split()))
			cur += 1
		sol.append(solve(tribes))
		
	return sol

#############################
	
def makestring(row):
	# make a list into a string separated by spaces
	return ''.join([' '+str(i) for i in row])[1:]

def olwrite(fname, answers):
	# write outputs to file line by line [one-line outputs]
	f = open(fname, 'w')
	lines = ['Case #'+str(i+1)+': '+str(answers[i])+'\n' for i in xrange(len(answers))]
	f.writelines(lines)
	f.close()
	return
	
def sread(fname):
	f = open(fname, 'r')
	res = [x.strip() for x in f.readlines()]
	f.close()
	return res
	

stuff = sread(INPUT_NAME)
answers = fullsol(stuff)
olwrite(OUTPUT_NAME, answers)




	