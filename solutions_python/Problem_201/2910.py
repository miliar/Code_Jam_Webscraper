#!/usr/bin/python3

def solve(n,k) :	
	liste = [n]
	while (k != 0) :
		right = 0
		left = 0
		
		maxlen = liste[0]
		pos = 0
		for i in range(len(liste)) :
			if liste[i] >= maxlen :
				pos = i
				maxlen = liste[i]

		if maxlen %2 == 0 :
			left = int(maxlen/2 - 1)
			right = int(maxlen/2)
		else : 
			left = int(maxlen/2)
			right = int(maxlen/2)

		liste[pos] = right
		liste.insert(pos,left)
		k -= 1

	return left,right
	

testCase = int(input())
for case in range(1,testCase+1) :
	n,k = [int(x) for x in input().split()]
	l,r = solve(n,k)
	print ('Case #{}: {} {}'.format(case,max(l,r),min(l,r)))