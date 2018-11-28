import re, sys

filename = sys.argv[1]

data = open(filename, 'r').read().splitlines()
params = data[0].split(" ")

L = params[0]
D = params[1]
N = params[2]

W = []
for i in data[1:(int(D) + 1)]:
	W += [i]

###################
P = []
for i in data[(int(D) + 1):(int(D) + int(N) + 1)]:
	P += [i]
	
#q = P[1]
#print q

###################
#Make pats
NP = []
for pi in P:
	addbar = 0
	newP = ""
	for i in pi:
		if i == ")":
			addbar = 0
			
		if addbar == 1:
			newP = newP + i + "|"
		else:
			newP = newP + i
			
		if i == "(":
			addbar = 1	
			
	newP = re.sub("\|\)", ")", newP)
	NP += [newP]
	
idx = 0
for npi in NP:
	idx += 1
	matches = 0
	for wi in W: 
		if re.match(npi, wi):
			matches	 += 1
	print "Case #" + str(idx) + ": " +  str(matches)
