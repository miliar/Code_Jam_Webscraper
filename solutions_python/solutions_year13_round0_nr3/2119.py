#!/usr/bin/env python

def isPalindrome(a):
	a = str(a)
	if len(a)<2:
		return True
	if a[0]!=a[-1]:
		return False 
	else:
		return isPalindrome(a[1:-1])

if __name__=="__main__":
	T = int(input())
	for i in range(0,T):
		t = input()
		l,u = int(t.partition(" ")[0]), int(t.partition(" ")[2])
		c=0
		for j in range(l,u+1):
			if isPalindrome(j) and j**0.5%1==0 and isPalindrome(int(j**0.5)):
				c=c+1
		print("Case #",i+1,": ",c,sep="")