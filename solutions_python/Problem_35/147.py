import psyco
psyco.full()

from numpy import array
lines = open("B-large.in").read().split("\n")

n = int(lines[0])

#reversed direction
def canFlow(m, l1, c1, l2, c2):
	return (0<=l1<len(m) and 0<=l2<len(m) and
			0<=c1<len(m[0]) and 0<=c2<len(m[0]) and
			m[l2][c2] > m[l1][c1] )
			
def isSink(m, l, c):
	return  not(canFlow(m,l-1,c,l,c) or canFlow(m,l+1,c,l,c)or
			canFlow(m,l,c-1,l,c) or canFlow(m,l,c+1,l,c))
			
def createMap(h, w, flow, flow_next, m):
	isChanged = True
	while isChanged:
		isChanged = False		
		for l in xrange(h):
			for c in xrange(w):
				if True:#flow[l][c]=="#": #not visited
					min, f = m[l][c], flow[l][c]					
					if 0<=l-1 and flow[l-1][c]!="#":
						if min > m[l-1][c]:
							min = m[l-1][c]
							f = flow[l-1][c]
					if 0<=c-1 and flow[l][c-1]!="#":
						if min > m[l][c-1]:
							min = m[l][c-1]
							f = flow[l][c-1]
					if c+1<w and flow[l][c+1]!="#":
						if min > m[l][c+1]:
							min = m[l][c+1]
							f = flow[l][c+1]					
					if l+1<h and flow[l+1][c]!="#":
						if min > m[l+1][c]:
							min = m[l+1][c]
							f = flow[l+1][c]					
					if f!=flow[l][c]:
						isChanged = True
						flow_next[l][c] = f		
		flow = flow_next.copy()
	return flow
		
currentLine = 1
output = []
for i in xrange(1, n+1):
	h, w = [int(x) for x in lines[currentLine].split()]
	currentLine+=1
	m = []
	flow = []
	
	for j in xrange(h):
		m.append([int(x) for x in lines[currentLine].split()])		
		currentLine+=1
		#labels
		flow.append(["#"]*w)
	
	#chr(97) == 'a'
	k = 97
	#sinks
	for l in xrange(h):	
		for c in xrange(w):			
			if isSink(m, l, c):
				flow[l][c] = chr(k)
				k+=1
	
	m, flow = array(m), array(flow)
	flow_next = flow.copy()
	
	flow = createMap(h, w, flow, flow_next, m)	
	
		#print m
		#print flow		
		#raw_input()
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	indexes = {}
	index = 0
	for l in xrange(h):
		for c in xrange(w):
			if not indexes.has_key(flow[l][c]):
				indexes[flow[l][c]] = index
				index+=1
	for l in xrange(h):
		for c in xrange(w):
			flow[l][c] = alphabet[indexes[flow[l][c]]]  
	soutput = "Case #"+str(i)+":\n"
	soutput += "\n".join([" ".join(x) for x in flow])
	output.append( soutput)
open("result.txt","w").write( "\n".join(output))