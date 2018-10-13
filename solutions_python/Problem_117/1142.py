from math import *;
#INPUT_NAME = 'B-small-attempt0.in'
#OUTPUT_NAME = 'B-small.out'
INPUT_NAME = 'B-large.in'
OUTPUT_NAME = 'B-large.out'
	
def solve(G):
	Mrows = [max(x) for x in G]
	Mcols = [max([G[i][j] for i in xrange(len(G))]) for j in xrange(len(G[0]))]
	for i in xrange(len(G)):
		for j in xrange(len(G[0])):
			if(G[i][j] != Mrows[i] and G[i][j] != Mcols[j]):
				return "NO"
	return "YES"		

def fullsol(slst):
	T = int(slst[0]) # number of test cases
	cur = 1
	answers = [];
	for i in xrange(T):
		(N,M) = map(int, slst[cur].split())
		G = [map(int, slst[cur+i+1].split()) for i in xrange(N)]
		cur += N+1
		answers.append(solve(G))
		
	return answers
	
	
def makestring(row):
	# make a list into a string separated by spaces
	return ''.join([' '+str(i) for i in row])[1:]

def olwrite(fname, answers):
	# write outputs to file line by line [one-line outputs]
	f = open(fname, 'w')
	lines = ['Case #'+str(i+1)+': '+answers[i]+'\n' for i in xrange(len(answers))]
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


	