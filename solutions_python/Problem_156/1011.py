#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

def getTimeFromPlates(plates):
	time = 0
	div = 0
	needMoreTime = True
	# while (needMoreTime):
	# 	print time,div,plates
	# 	p = max(plates)
	# 	if p<=3:
	# 		time = max([time,p])
	# 		return time
	# 	elif p>time:
	# 		plates.remove(p)
	# 		# while (p>time):
	# 		div+=1
	# 		p2= p/2 if p%2==0 else p/2+1
	# 		# for x in range(1,int(math.sqrt(p))):
	# 			# plates.append(p-x)
	# 		plates.append(p2)
	# 		plates.append(p-p2)
	# 		time = max(plates)+div
	# 	else:
	# 		needMoreTime = False
	time = max(plates)
	while(True):
		# print time,div,plates
		p = max(plates)
		p2= p/2 if p%2==0 else p/2+1
		if p<=3:
			time = max([time,p])
			return time
		if p2+div+1>=time:
			break
		else:
			div+=1
			plates.remove(p)
			plates.append(p2)
			plates.append(p-p2)
			time2 = max([p2,max(plates)])+div
			if time2>time:
				break
			else:
				time=time2

	# print time,div,plates
	return time

def main():
	# filestr = 'B-small-attempt0'
	# filestr = 'B-large'
	filestr = 'B-verysmall'
	fin = open(filestr+'.in.txt','r')
	fout = open(filestr+'.out.txt','w')

	lines = fin.read().splitlines()
	T = int(lines[0])
	curr_line = 1
	for i in range(T):
		D = int(lines[curr_line])
		plates = [int(x) for x in lines[curr_line+1].split(' ')]	

		dinerTime = getTimeFromPlates(plates)

		str=  'Case #%d: %d'%(i+1,dinerTime)
		fout.write(str+'\n')
		print str#+' '+lines[curr_line+1]

		curr_line+=2

	fin.close()
	fout.close()


if __name__ == "__main__":
	main()
