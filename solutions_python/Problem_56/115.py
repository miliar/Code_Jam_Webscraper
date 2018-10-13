# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
CASES = int(fin.readline())
#print CASES
for case in range(1,CASES+1):
	NK = map(int,fin.readline().split())
	N=NK[0]
	K=NK[1]
	inp = [fin.readline().split() for i in range(0,N) ]
	code = [inp[i][0] for i in range(0,N)]
	brot = []
	for i in range(N-1,-1,-1):
		x = []
		for j in range(0,N):
			if(code[i][j]!= '.'):
				x.append(code[i][j]);
		k = ['.' for p in range(0,N-len(x))]	
		k = k + x
#print k
		brot.append(k)
	rot = map(list,zip(*brot))

#	print "================"
#	for i in range(0,N):
#		print rot[i]
	cal = [[[ 0 for i in range(0,N)] for j in range(0,N)] for g in range(0,4)]
	for i in range(1,N):
		for j in range(1,N):
			if(rot[i][j] == rot[i-1][j-1]):
				if(rot[i][j] == 'R'):
					cal[0][i][j] = cal[0][i-1][j-1] +1
				elif (rot[i][j] == 'B'):
					cal[0][i][j] = cal[0][i-1][j-1] - 1

	for i in range(1,N):
		for j in range(0,N):
			if(rot[i][j] == rot[i-1][j]):
				if(rot[i][j] == 'R'):
					cal[1][i][j] = cal[1][i-1][j] +1
				elif (rot[i][j] == 'B'):
					cal[1][i][j] = cal[1][i-1][j] - 1

	for i in range(0,N):
		for j in range(1,N):
			if(rot[i][j] == rot[i][j-1]):
				if(rot[i][j] == 'R'):
					cal[2][i][j] = cal[2][i][j-1] +1
				elif (rot[i][j] == 'B'):
					cal[2][i][j] = cal[2][i][j-1] - 1

	for i in range(1,N):
		for j in range(N-2,-1,-1):
			if(rot[i][j] == rot[i-1][j+1]):
				if(rot[i][j] == 'R'):
					cal[3][i][j] = cal[3][i-1][j+1] +1
				elif (rot[i][j] == 'B'):
					cal[3][i][j] = cal[3][i-1][j+1] - 1
	f1 = 0
	f2 = 0
#	print K 
#	print cal
	for i in range(0,4):
		for j in range(0,N):
			for p in range(0,N):
				if(cal[i][j][p] >= K-1):
					f1  = 1
#				print i,j,p
				if(cal[i][j][p] <= 1-K):
					f2 = 1
#					print i,j,p
#	print f1, f2
	if(f1 ==0 and f2 == 0):
		print "Case #%d: Neither" % (case)
	if(f1 ==1 and f2 == 0):
		print "Case #%d: Red" % (case)
	if(f1 ==0 and f2 == 1):
		print "Case #%d: Blue" % (case)
	if(f1 ==1 and f2 == 1):
		print "Case #%d: Both" % (case)
    
