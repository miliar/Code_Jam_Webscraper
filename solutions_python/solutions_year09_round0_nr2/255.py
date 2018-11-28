#! /usr/bin/env python

input = open("/Users/benzax/code_jam/input.txt",'r')

output = open("/Users/benzax/code_jam/output.txt",'w')

N = int(input.readline())


for i in xrange(1,N+1):
	line = input.readline()
	arr = line.split(" ")
	H = int(arr[0])
	W = int(arr[1])

	alt = []
	
	for j in xrange(0, H):
		alt.append((input.readline()[:-1]).split(" "))
		
	
	label = []
	for j in range(0,H):
		label.append( [ x + j*W for x in xrange(0,W) ] )
		
	
	for j in range(0, H):
		for k in range(0, W):
			cur = alt[j][k]
			if j != 0 and alt[j-1][k] < cur:
				cur = alt[j-1][k]
				label[j][k] = label[j-1][k]
			if k != 0 and alt[j][k-1] < cur:
				cur = alt[j][k-1]
				label[j][k] = label[j][k-1]
			if k != W-1 and alt[j][k+1] < cur:
				cur = alt[j][k+1]
				label[j][k] = label[j][k+1]
			if j != H-1 and alt[j+1][k] < cur:
				cur = alt[j+1][k]
				label[j][k] = label[j+1][k]
				
	
	for j in range(0, H):
		for k in range(0, W):
			r = j
			c = k
			while r != label[r][c]/W or c != label[r][c]%W :
				l = label[r][c]
				r = l/W
				c = l%W
			
			r2 = j
			c2 = k
			while r2 != label[r][c]/W or c2 != label[r][c]%W :
				l = label[r2][c2]
				label[r2][c2] = label[r][c]
				r2 = l/W
				c2 = l%W
				
				
	alpha = { }
	
	index = ord('a')
	
	s = "Case #" + str(i) + ":\n"
	output.write(s)
				
	for j in range(0, H):
		for k in range(0, W):
			if label[j][k] not in alpha:
				alpha[ label[j][k] ] = chr(index)
				index += 1
			output.write(alpha[label[j][k]])
			if k < W-1:
				output.write(" ")
		output.write("\n")


	
