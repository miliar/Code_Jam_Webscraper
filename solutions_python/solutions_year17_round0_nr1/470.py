#coding: utf-8

def flip(l,i,K):
	for j in range(i,i+K):
		l[j] = 1-l[j]

def P1(p,K):
	n = 0
	for i in range(len(p)-K+1):
		if not(p[i]):
			n+=1
			flip(p,i,K)
			
	valid = True
	for i in range(len(p)-K+1,len(p)):
		valid = valid and p[i]
	
	if valid:
		return str(n)
	else:
		return "IMPOSSIBLE"



T = int(input())
for t in range(T):
	pancakes, K = input().split()
	K = int(K)
	pancakes = list(map(lambda x:0 if x=='-' else 1,list(pancakes)))
	
	print("Case #%d: %s"%(t+1,P1(pancakes,K)))
