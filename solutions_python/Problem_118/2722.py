from math import sqrt

def is_perfect(n):
	s = sqrt(n)
	if s!=int(s): return False
	if is_palindrome(int(s)):
		return True
	return False
	
def is_palindrome(n):
	s = str(n)
	l = len(s)
	if(l==1): return True
	for i in xrange((l/2)+1):
		if(s[i]!=s[l-i-1]):
			return False
	return True
	
memo = []
for i in xrange(1001): memo.append(-1)

def is_fas(n):
	if(memo[n]==-1):
		if(is_perfect(n) and is_palindrome(n)): memo[n] = True
		else: memo[n] = False
	return memo[n]
	
def count(a, b):
	c = 0
	for i in xrange(a, b+1):
		if is_fas(i):
			c+=1
	return c
	
if __name__ == '__main__':
	k = input()
	for i in xrange(k):
		inp = raw_input()
		inp2 = inp.split()
		print "Case #"+str(i+1)+": "+str(count(int(inp2[0]), int(inp2[1])))
	
