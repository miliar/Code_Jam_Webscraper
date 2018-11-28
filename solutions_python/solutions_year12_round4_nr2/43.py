#!/usr/bin/python
import sys
import math

def reorder(Rorder, pos):
	result = [0] * len(pos)
	
	i = 0
	for (index,value) in Rorder:
		result[index] = pos[i]
		i+=1

	return result
		
	
def calculate_positions(W,L,R):
	Rorder = sorted(enumerate(R), key=lambda x: x[1])
	Rorder.reverse()
	
	R= [] 
	for (index,value) in Rorder:
		R.append(value)
	
	pos = []
	
	start_y = 0
	current = 0
	start_x = 0
	
	#print "W:",W, "L:", L
	#print R
	#print start_x,start_y	
	
	while (current < len(R) and start_y < L):
		maxradius = R[current]
		#print "Max radius iter ", maxradius

		while (start_x < W and current < len(R)) :
			#print "Current: ",current
			radius = R[current]
			pos_x = start_x
			pos_y = start_y
			
			#print "Insert"
			pos.append(str(pos_x) + ' ' + str(pos_y))
			current += 1
			if (current < len(R)):			
				start_x += radius + R[current]

		if (current < len(R)):
			start_y += maxradius + R[current]
		start_x = 0
		
	if (len(pos) != len(R)):
		print "err",len(pos),len(R)
		sys.exit(1)
	
	return reorder(Rorder,pos)

def main():
	T = int(sys.stdin.readline())
	
	for i in xrange(T):
		parts = sys.stdin.readline().strip().split(' ')
		N = int(parts[0])
		W = int(parts[1])
		L = int(parts[2])
		
		parts = sys.stdin.readline().strip().split(' ')
		R = []
		for j in xrange(N):
			R.append(int(parts[j]))
			
		#print R
			
		pos = calculate_positions(W,L,R)
		pos_str = ' '.join(pos)
		print "Case #" + str(i+1) + ": " + pos_str
main()
