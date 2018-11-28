import math

def rec(n, k) :
	if k == 0 :
		return [None, None]
	if k == 1 :
		return [math.ceil((n-1)/2), math.floor((n-1)/2)]
	
	a_n = math.ceil((n-1)/2)
	a_k = math.ceil((k-1)/2)
	b_n = math.floor((n-1)/2)
	b_k = math.floor((k-1)/2)
	
	if a_k > b_k :
		return rec(a_n, a_k)
	elif b_n < a_n :
		return rec(b_n, b_k)
	else :
		return rec(a_n, a_k)
		
	if b == [None, None] or a != [None,None] and a < b :
		return a
	return b

t = int(input())
for i in range(0,t) :
	n,k = input().split()
	n = int(n)
	k = int(k)
	r = rec(n,k)
	print("Case #", i+1, ": ", r[0], " ", r[1], sep="")