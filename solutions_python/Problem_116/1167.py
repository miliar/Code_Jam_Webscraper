from math import *;
INPUT_NAME = 'A-large.in'
OUTPUT_NAME = 'A-large.out'

def modify(x,o,val):
	if(val=='O'):
		x = False
	elif(val=='X'):
		o = False
	elif(val=='.'):
		(x,o) = (False,False)
	return (x,o)
	
def solve(x):	
	# check rows	
	full = True
	(xd1, od1,xd2,od2) = (True,True,True,True)
	for i in xrange(4):
		(xd1,od1) = modify(xd1,od1,x[i][i])
		(xd2,od2) = modify(xd2,od2,x[i][3-i])
			
		(xh,oh,xv,ov) = (True,True,True,True)
		for j in xrange(4):
			if(x[i][j]=='.'):
				full = False
			(xh,oh) = modify(xh,oh,x[i][j])
			(xv,ov) = modify(xv,ov,x[j][i])
			
		if(xh|xv):
			return 'X won'
		elif(oh|ov):
			return 'O won'
			
	if(xd1|xd2):
		return 'X won'
	elif(od1|od2):
		return 'O won'
	elif(full):
		return 'Draw'
	else:
		return 'Game has not completed'
			

def fullsol(slst):
	T = int(slst[0]) # number of test cases
	return [solve(slst[1+5*i:5+5*i]) for i in xrange(T)]
	
	
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


	