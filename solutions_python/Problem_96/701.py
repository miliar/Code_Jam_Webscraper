#! /usr/bin/env python3

def decission(score, p):
	
	# corner cases
	if score == 0 and p > 0:
		return -1
	if score == 1 and p > 1:
		return -1	
	
	val = round(p - score/3.0, 2)
	
	if val <= 0.67:
		return 0
	elif val <= 1.33:
		return 1
	return -1
	
if __name__ == '__main__':
	T = int(input())
	for i in range(T):
		row = input().split()
		n = int(row[0])
		s = int(row[1])
		p = int(row[2])
		t = row[3:]
		
		nsup = 0
		sup = 0
		for j in t:
			d = decission(int(j),p)
			if d == 0:
				nsup += 1
			elif d == 1:
				sup += 1
		score = nsup + min(s,sup)
		print("Case #" + str(i+1) + ": " + str(score))
		
			
			 
		


	
