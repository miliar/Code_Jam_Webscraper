#!/usr/bin/python

import sys

lines = []

i=-1
for line in sys.stdin.readlines():
	i+=1
	if i is 0:
		numlines = int(line)
	else:
		lines.append(line.strip())

def max (g):
	""" What is the maximum value in this triple?
	"""
	g.sort()
	return g[-1]

def score (g):
	""" What is the score of this triple?
	"""
	o = 0
	for e in g:
		o+=e
	return o

def suprising (g):
	""" Is the triple g suprising?
	"""
	g.sort()
	return g[0]+2==g[-1]
	# you may be wondering why i keep sorting g, even though i know 
	# it already is. its cause I can't help taking into account edge 
	# cases of things. yes yes I know none of my code has error checking 
	# in it. I'm in a hurry. I just can't help it sometimes
	# you may also wonder why i even wrote this function...
	
def valid (g):
	""" ensure that the elements of g are not out of range (0-10)
	"""
	for e in g:
		if not 0<=e<=10:
			return False
	return True
	
def possible (score):
	""" given the score of the triple, what are the 
	    possible triples which can make this score
	    output[0] will be unsuprising, output[1] will
	    be suprising
	"""
	core = ( ((0,0,0),(-1,0,1)),	#0
		 ((0,0,1),(-1,1,1)),	#1
		 ((0,1,1),( 0,0,2)) )	#2
	#the last one should have been ((-1,0,0),(-1,-1,1))
	# but only if you like mathematical beauty in things
	
	out = []
	for e in core[score%3]:
		o = []
		for f in e:
			o.append(f+int(score/3))
		out.append(o)
	
	return out
	#I could go to the trouble of explaining this madness, but will anyone read it?

#set of possible scores for each googler
def setscores(ti):
	""" This returns the list of unsuprising outputs for each googler, and
	    the list of the most optimistic scores for each googler
	    this will not always be the suprising output
	    since some outputs are not valid for edge cases score=0,1,29 and 30
	"""
	unsuprising = []
	optimistic = []
	for t in ti:
		p = possible(t)
		unsuprising.append(p[0])
		#if the suprising one is an edge case then we just use the unsuprising one
		if valid(p[1]):
			optimistic.append(p[1])
		else:
			optimistic.append(p[0])
	return (unsuprising,optimistic)

def rankbybest(ti, unsuprising, optimistic):
	""" ranks a list of scores and the possible combinations that 
            make those scores, ranks by max unsuprising score
	"""
	scores = []
	for i in range(len(ti)):
		scores.append((ti[i],unsuprising[i],optimistic[i]))
	
	scores.sort()
	return scores	# note that the output is odd now

c = 0
for line in lines:
	c+=1
	ints = line.split()
	N = int(ints[0])
	S = int(ints[1])
	p = int(ints[2])
	#why you haz no error checking???
	ti = [int(e) for e in ints[3:N+3]]
	
	u,o = setscores(ti)
	scores = rankbybest(ti, u, o)
	
	suprising = 0
	finallist = []	#from now we may as well just add up the list of p values
	for i in range(len(scores)-1,-1,-1):
		e = scores[i][1]	#assume we are going to use the unsuprising one unless:
		
		#we only start using suprising one if the unsuprising ones aren't big enough
		#otherwise we don't want to waste them
		if max(scores[i][1])<p:
			#we also don't want to waste a suprising one if we know its an edge case (they are the same)
			if 2<scores[i][0]<29:
				# if we are all out of suprise then stop being suprised
				if suprising<S:
					suprising+=1
					e = scores[i][2]
		
		finallist.append(max(e))	#OMG we actually used one of those functions up there
		
	#now all thats left to do is see how many of them are greater than or equal to p
	count = 0
	for e in finallist:
		if e>=p:
			count+=1

	print ("Case #%s: %d" % (c,count),)
	
#print (possible(28),)