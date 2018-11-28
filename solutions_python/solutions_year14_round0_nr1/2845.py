#!/usr/bin/python

#@ucefkh 2014 fb.com/ucefkh


def findCard(a,b,c):
	#~ print "A",c[0]
	#~ for x in range(1,5):
		#~ print a[x-1]
	#~ print "B",c[1]
	#~ for x in range(1,5):
		#~ print b[x-1]
	#~ if a[c[0]-1][x-1] in b[c[1]-1]:
	#~ print b[c[1]-1]
	po = 0
	g = 0
	for x in range(1,5):
		if a[c[0]-1][x-1] in b[c[1]-1]:
			po+=1
			g = a[c[0]-1][x-1]
	if po > 0 and po < 2:
		return g
	elif po == 0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!" 
	


f = file("A-small-attempt0.in")

cases = int(f.readline())
n=cases
choices = [0,0]
grid = [[],[],[],[]],[[],[],[],[]]


while cases :
	print "Case #{0}:".format(n-cases+1),
	for j in range(0,2):
		choices[j] = int(f.readline().strip())
		for i in range(1,5):
			grid[j][i-1] = map(int,f.readline().strip().split(' '))
	print findCard(grid[0],grid[1],choices)
	#~ print choices[0],choices[1]
	#~ if cases != n:
		#~ print "\n"
	cases-=1
