#usr/bin/python
from __future__ import division
import sys
import random

fin = open(sys.argv[1], "r")
fout = open("A.out", "w")

def check_validity(board, R, C):
	lets = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
	for let in lets:
		
		out = []
		rmin = 100
		rmax = -1
		cmin = 100
		cmax = -1
		for r in range(R):
			for c in range(C):
				if board[r][c] == let:	
					out.append((r,c))
					if r > rmax:
						rmax = r
					if r < rmin:
						rmin = r
					if c > cmax:
						cmax = c
					if c < cmin:
						cmin = c
		#print(out)				
		if out!=[]:
			for r in range(rmin, rmax+1):
				for c in range(cmin, cmax+1):
					if (r,c) in out:
						out.remove((r,c))
					else:
						return False
		if out!=[]:
			return False
	return True			

T = int(fin.readline())
for ii in xrange(T):
	R, C = map(int,fin.readline().split(' '))
	inp = []
	for r in range(R):
		new_line = fin.readline().rstrip()
		inp.append(new_line)
	pos_lets = list(set([item for sublist in inp for item in sublist]))
	if '?' in pos_lets:
		pos_lets.remove('?')
	print pos_lets

	pos = [[[] for c in range(C)] for r in range(R)]
	print pos

	for c in range(C):
		new = '?'
		for r in range (R):
			let = inp[r][c]
			if let != '?':
				new = let
				#print pos[r][c]
				pos[r][c] = [let]
				#print (r, c, pos)
			else:
				if new != '?':
					pos[r][c].append(new)				
	for c in range(C):
		new = '?'
		for r in reversed(range (R)):
			let = inp[r][c]
			if let != '?':
				new = let
				pos[r][c] = [let]
			else:
				if new != '?':
					pos[r][c].append(new)

	for r in range(R):
		new = '?'
		for c in range (C):
			let = inp[r][c]
			if let != '?':
				new = let
				pos[r][c] = [let]
			else:
				if new != '?':
					pos[r][c].append(new)				
	for r in range(R):
		new = '?'
		for c in reversed(range(C)):
			let = inp[r][c]
			if let != '?':
				new = let
				pos[r][c] = [let]
			else:
				if new != '?':
					pos[r][c].append(new)								

	#print pos	
	#if check_validity([['A'],['B']],2,1):
	#		print 'YES'
	print inp
	print pos
	while True:
		board = [[[] for c in range(C)] for r in range(R)]
		for r in range(R):
			for c in range(C):
				#print pos[r][c]
				if inp[r][c] != '?':
					pos[r][c] = [inp[r][c]]
				else:
					pos[r][c] = pos_lets	
				board[r][c] = random.choice(pos[r][c])
		#print inp, pos, board
		if check_validity(board, R, C) == True:
			break				
	print ii
	fout.write("Case #" + str(ii+1) + ":" + "\n")
	for r in range(R):
		fout.write( ''.join(board[r])+ "\n")		
	#fout.write(' '.join(map(str,sol_board_true[i])) + "\n")			
	