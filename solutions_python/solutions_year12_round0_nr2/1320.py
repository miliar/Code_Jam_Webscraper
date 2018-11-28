# -*- coding: utf-8 -*-
import sys



qNum = int(sys.stdin.readline()[0:-1])
for q in xrange(qNum):

	line = [int(x) for x in sys.stdin.readline()[0:-1].split(' ') ]
	
	N = line[0]
	supcase = line[1]
	p = line[2]
	ps = line[3:]
	score = []
	sup = []

	#if q != 2:
	#	continue

	for n0 in xrange(0,11):
		for n1 in xrange(n0,11):
			for n2 in xrange(n1,11):

				sum = n0 + n1 + n2
				if n2 < p :
					continue

				# 全部同じ
				if n2 == n1 and n1 == n0:
					#print "!," + str(n0) + " " + str(n1) + " " + str(n2)
					score.append(sum)
					continue
				
				# n0のみ違う
				if n2 == n1 and n1 - n0 == 1:
					score.append(sum)
					continue

				# n1のみ違う
				if n2 - n1 == 1 and n1 == n0:
					score.append(sum)
					continue


				# 全部違う (1,2,3)
				if n2 - n1 == 1 and n1 - n0 == 1 :
					sup.append(sum)
					continue


				# n0のみ違う
				if n1 - n0 == 2 and n1 == n2 :
					sup.append(sum)
					continue
				

				# n2のみ違う
				if n2 - n1 == 2 and n0 == n1 :
					#print "!," + str(n0) + " " + str(n1) + " " + str(n2)
					sup.append(sum)
					continue

	#print score
	#print sup

	point = 0
	for num in ps:
		#print num
		if num in score :
			point+=1
			continue
		if num in sup and supcase > 0:
			point+=1
			supcase-=1
	
	print "Case #" + str(q+1) + ": " + str(point)

	
